import asyncio
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ingestion.scraper import SHLCatalogScraper

async def main():
    print("Booting SHL Data Ingestion Pipeline...")
    print("Note: Phase 2 deep scraping requires visiting 377+ individual pages.")
    print("Please allow 5-10 minutes for the pipeline to complete to avoid IP blocks.\n")
    
    scraper = SHLCatalogScraper()
    df = await scraper.scrape_catalog()
    
    if not df.empty:
        scraper.save_data(df, filepath="data/raw/shl_catalog_raw.csv")
        print("\n" + "="*50)
        print(f" SUCCESS! {len(df)} detailed assessments safely extracted.")
        print("="*50)
    else:
        print(" CRITICAL: Pipeline failed or yielded zero results.")

if __name__ == "__main__":
    asyncio.run(main())