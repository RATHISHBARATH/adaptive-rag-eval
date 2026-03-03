import asyncio
import re
import json
import logging
from bs4 import BeautifulSoup
import pandas as pd
from typing import List, Dict
from pathlib import Path
from playwright.async_api import async_playwright

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("SHL_Ingestion")

class SHLCatalogScraper:
    """
    Production-grade Async Scraper using Playwright.
    Handles dynamic DOM rendering, pagination, and deep metadata extraction.
    """
    BASE_URL = "https://www.shl.com/solutions/products/product-catalog/"
    
    def __init__(self):
        self.assessment_links: List[Dict[str, str]] = []
        self.detailed_assessments: List[Dict] = []

    async def scrape_catalog(self) -> pd.DataFrame:
        logger.info("Initializing Playwright Engine...")
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            page = await context.new_page()



            # ==========================================
            # PHASE 1: Paginate and Collect URLs
            # ==========================================
            
            
            try:

                logger.info(f"Navigating to {self.BASE_URL}")
                await page.goto(self.BASE_URL, wait_until="networkidle", timeout=60000)
                
                while True:
                    await page.wait_for_timeout(3000) 
                    html = await page.content()
                    soup = BeautifulSoup(html, "html.parser")
                    
                    for link in soup.find_all("a", href=True):
                        href = link.get("href", "")
                        name = link.get_text(strip=True)
                        
                        if ("/view/" in href.lower() or "product-catalog/" in href.lower()) and name:
                            if len(name) > 3 and name.lower() not in ["next", "previous", "close", "read more"]:
                                full_url = href if href.startswith("http") else f"https://www.shl.com{href}"
                                self.assessment_links.append({"name": name, "url": full_url})
                                
                    next_btn = page.locator("a:has-text('Next'), button:has-text('Next'), .next, [aria-label*='Next']")
                    if await next_btn.count() > 0:
                        is_disabled = await next_btn.first.get_attribute("disabled")
                        class_name = await next_btn.first.get_attribute("class") or ""
                        if is_disabled is not None or "disabled" in class_name.lower():
                            break
                        try:
                            await next_btn.first.click(force=True)
                        except Exception:
                            break
                    else:
                        break

                df_links = pd.DataFrame(self.assessment_links).drop_duplicates(subset=["url"])
                df_links = df_links[~df_links['name'].str.contains("pre-packaged|prepackaged", case=False, na=False)]
                urls_to_scrape = df_links.to_dict('records')
                logger.info(f"Phase 1 Complete. Mapped {len(urls_to_scrape)} unique individual assessments.")




                # ==========================================
                # PHASE 2: Deep Scrape Individual Pages
                # ==========================================



                logger.info("Starting Phase 2: Deep metadata extraction (This will take a few minutes)...")
                for i, item in enumerate(urls_to_scrape):
                    if i % 50 == 0: 
                        logger.info(f"Progress: [{i}/{len(urls_to_scrape)}] assessments processed.")
                        
                    try:
                        await page.goto(item['url'], wait_until="domcontentloaded", timeout=25000)
                        html = await page.content()
                        soup = BeautifulSoup(html, "html.parser")
                        text_content = soup.get_text(separator=" ", strip=True).lower()
                        
                        
                        
                        duration_match = re.search(r'(?:duration|time).*?(\d+)\s*min', text_content)
                        duration = int(duration_match.group(1)) if duration_match else 0
                        

                        test_types = []
                        if "ability" in text_content or "aptitude" in text_content: test_types.append("Ability & Aptitude")
                        if "biodata" in text_content or "situational" in text_content: test_types.append("Biodata & Situational Judgement")
                        if "competenc" in text_content: test_types.append("Competencies")
                        if "knowledge" in text_content or "skills" in text_content: test_types.append("Knowledge & Skills")
                        if "personality" in text_content or "behavior" in text_content: test_types.append("Personality & Behavior")
                        if "simulation" in text_content: test_types.append("Simulations")
                        if not test_types: test_types.append("Knowledge & Skills") 


                        desc_tag = soup.find("meta", {"name": "description"})
                        description = desc_tag["content"] if desc_tag else "Comprehensive SHL Assessment"

                        self.detailed_assessments.append({
                            "name": item['name'],
                            "url": item['url'],
                            "description": description,
                            "duration": duration,
                            "adaptive_support": "Yes" if "adaptive" in text_content or "item response" in text_content else "No",
                            "remote_support": "Yes" if "remote" in text_content or "online" in text_content else "No",
                            "test_type": json.dumps(test_types) 
                        })
                    except Exception as e:
                        logger.debug(f"Failed deep scrape for {item['url']}, using defaults. Error: {e}")
                        self.detailed_assessments.append({
                            "name": item['name'], "url": item['url'], "description": "Assessment details unavailable.",
                            "duration": 0, "adaptive_support": "No", "remote_support": "Yes", "test_type": '["Knowledge & Skills"]'
                        })
            finally:
                await browser.close()
                
        return pd.DataFrame(self.detailed_assessments)

    def save_data(self, df: pd.DataFrame, filepath: str = "data/raw/shl_catalog_raw.csv"):
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(path, index=False)
        logger.info(f" Data successfully serialized to {filepath}")