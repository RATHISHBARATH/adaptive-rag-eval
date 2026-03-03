from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    PROJECT_NAME: str = "SHL Assessment Recommendation API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Model Configurations
    GOOGLE_API_KEY: str = "" # Pydantic will pull this from your .env file
    LLM_MODEL_NAME: str = "gemini-2.5-flash"
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"
    
    # Storage Paths
    VECTOR_STORE_PATH: str = "data/vector_store"
    RAW_DATA_PATH: str = "data/raw/shl_catalog_raw.csv"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    return Settings()