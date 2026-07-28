from pydantic import BaseModel , Field , field_validator
from app.config import get_settings

settings = get_settings()

class TranslationRequest(BaseModel):
    # Corps de la requete pour la traduction
    text: str = Field(... ,
                       min_length=1 , 
                       max_length=settings.max_text_length,
                       description="Texte en Francais a traduire en ewe",
                       )

    @field_validator("text")
    @classmethod
    def text_not_empty(cls, value: str) -> str:
        stripped=value.strip()
        if not stripped:
            raise ValueError("Le texte ne doit pas etre vide ou composer uniquement d'espaces")
        return stripped

class TranslationResponse(BaseModel):
    # Corps de la reponse pour la traduction
    source_text: str
    translated_text: str
    source_lang: str = settings.source_lang
    target_lang: str = settings.target_lang

class HealthResponse(BaseModel):
    # Reponse du endpojt /health
    model_config = {"protected_namespaces": ()}
    status: str
    model_loaded: bool

class ErrorResponse(BaseModel):
    # Format de la reponse des erreurs renvoyes par L'api
    error: str
    detail: str | None = None

