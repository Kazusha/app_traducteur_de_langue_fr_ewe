from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # Hugging Face api 
    hf_repo_id: str ="liman21/nllb-fr-ewe-midjie21"
    hf_token: str = ""
    
    api_title: str = "Traducteur Français-Ewé"
    max_text_length: int = 200
    allowed_origins: list[str] = ["http://localhost:3000"]

    rate_limit: str = "5/minute"

    source_lang: str = "fra_Latn"
    target_lang: str = "ewe_Latn"

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }

@lru_cache()
def get_settings() -> Settings:
    return Settings()