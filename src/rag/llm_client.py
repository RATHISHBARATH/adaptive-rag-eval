import os
import re
import json
import logging
import asyncio
import aiohttp
import sys
from bs4 import BeautifulSoup
from typing import Dict, Any
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from src.api.schemas import RecommendationResponse
from src.rag.prompts import shl_prompt

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("RAG_Engine")

class SHLRecommender:
    def __init__(self, vector_store_path: str = "data/vector_store"):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("CRITICAL: GOOGLE_API_KEY missing from .env file.")

        logger.info("Loading FAISS Vector Database in memory...")
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vector_store = FAISS.load_local(
            vector_store_path, 
            embeddings, 
            allow_dangerous_deserialization=True
        )

        logger.info("Initializing Google Gemini LLM...")
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash", 
            temperature=0.0,          
            google_api_key=self.api_key
        )

    async def _async_scrape_url(self, url: str) -> str:
        """Deep parses a JD URL if the user provides a link instead of text."""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=10) as response:
                    if response.status == 200:
                        html = await response.text()
                        soup = BeautifulSoup(html, "html.parser")
                        return " ".join([p.get_text(strip=True) for p in soup.find_all("p")])[:3000]
            return ""
        except Exception as e:
            logger.warning(f"Failed to scrape JD URL {url}: {e}")
            return ""

    def _format_context(self, docs) -> str:
        """Serializes FAISS metadata into a text block for the LLM context window."""
        return "\n".join([
            f"Name: {d.metadata.get('name')}\nURL: {d.metadata.get('url')}\n"
            f"Desc: {d.metadata.get('description')}\nDur: {d.metadata.get('duration')}\n"
            f"Adaptive: {d.metadata.get('adaptive_support')}\nRemote: {d.metadata.get('remote_support')}\n"
            f"Type: {d.metadata.get('test_type')}\n---" 
            for d in docs
        ])

    async def get_recommendation(self, query: str, top_k: int = 15) -> Dict[str, Any]:
        processed_query = query
        urls = re.findall(r'https?://\S+', query)
        
        if urls:
            logger.info("URL detected. Extracting Job Description context...")
            scraped_jd = await self._async_scrape_url(urls[0])
            if scraped_jd:
                processed_query = f"Original Query: {query}\n\nJD Context:\n{scraped_jd}"
                

        docs = self.vector_store.similarity_search(processed_query, k=top_k)
        context = self._format_context(docs)
        
        
        try:
            prompt_val = shl_prompt.format(query=processed_query, context=context)
            response = await self.llm.ainvoke(prompt_val)
            
            clean_json = response.content.strip()
            if clean_json.startswith("```json"): clean_json = clean_json[7:]
            if clean_json.endswith("```"): clean_json = clean_json[:-3]
                
            data = json.loads(clean_json.strip())
            validated_data = RecommendationResponse(**data)
            return validated_data.model_dump()
            
        except Exception as e:
            logger.warning(f"LLM API blocked ({type(e).__name__}). Activating Local Fallback Engine...")
            
            import ast
            k_tests, p_tests, other_tests = [], [], []

            for d in docs:
                meta = d.metadata
                try:
                    t_types = ast.literal_eval(meta.get("test_type", "[]"))
                except (ValueError, SyntaxError):
                    t_types = [meta.get("test_type", "")]
                    
                item = {
                    "url": str(meta.get("url", "")),
                    "name": str(meta.get("name", "Unknown Assessment")),
                    "adaptive_support": str(meta.get("adaptive_support", "No")),
                    "description": str(meta.get("description", ""))[:250] + "...",
                    "duration": int(meta.get("duration", 0)),
                    "remote_support": str(meta.get("remote_support", "Yes")),
                    "test_type": t_types if isinstance(t_types, list) else [str(t_types)]
                }
                
                is_k = any('Knowledge' in t or 'Skill' in t for t in item['test_type'])
                is_p = any('Personal' in t or 'Behavior' in t or 'Competenc' in t for t in item['test_type'])
                
                if is_k: k_tests.append(item)
                elif is_p: p_tests.append(item)
                else: other_tests.append(item)
                
            fallback_assessments = k_tests[:3] + p_tests[:3]
            if len(fallback_assessments) < 6:
                fallback_assessments += other_tests[:(6 - len(fallback_assessments))]
                
            return {"recommended_assessments": fallback_assessments}

async def test_engine():
    engine = SHLRecommender()
    test_query = "Need a Python developer who is good at collaborating with external teams and stakeholders."
    logger.info(f"Testing Query: '{test_query}'")
    
    result = await engine.get_recommendation(test_query)
    print("\n--- JSON RESPONSE ---")
    print(json.dumps(result, indent=2))
    await asyncio.sleep(0.25) 

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    try:
        asyncio.run(test_engine())
    except Exception as e:
        pass 