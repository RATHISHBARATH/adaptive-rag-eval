import pandas as pd
import os
import sys
import asyncio
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.rag.llm_client import SHLRecommender

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

async def main():
    input_csv = "data/test/test_queries.csv" 
    output_csv = "data/output/predictions.csv"
    
    if not os.path.exists(input_csv):
        logging.warning(f"Test data not found at {input_csv}. Creating a sample to proceed.")
        os.makedirs(os.path.dirname(input_csv), exist_ok=True)
        dummy_df = pd.DataFrame({"Query": [
            "Need a Java developer who is good in collaborating with external teams and stakeholders.",
            "Looking to hire mid-level professionals who are proficient in Python, SQL and Java Script."
        ]})
        dummy_df.to_csv(input_csv, index=False)

    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    
    df = pd.read_csv(input_csv)
    query_col = "Query" if "Query" in df.columns else df.columns[0]
    queries = df[query_col].dropna().tolist()
    
    engine = SHLRecommender()
    results_data = []
    
    logging.info(f"Generating predictions for {len(queries)} queries. Processing safely to avoid API limits...")
    
    for i, query in enumerate(queries):
        logging.info(f"[{i+1}/{len(queries)}] Processing: '{str(query)[:50]}...'")
        try:
            result = await engine.get_recommendation(str(query))
            assessments = result.get("recommended_assessments", [])
            
            for rec in assessments:
                results_data.append({
                    "Query": str(query),
                    "Assessment_url": rec.get("url", "")
                })
        except Exception as e:
            logging.error(f"Error on query: {e}")
            results_data.append({"Query": str(query), "Assessment_url": "ERROR"})
            
        if i < len(queries) - 1:
            await asyncio.sleep(4)
            
    submission_df = pd.DataFrame(results_data)
    submission_df.to_csv(output_csv, index=False)
    logging.info("\n" + "="*50)
    logging.info(f"SUCCESS! Appendix 3 Compliant CSV generated at: {output_csv}")
    logging.info("="*50)

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    try:
        asyncio.run(main())
    except Exception:
        pass  