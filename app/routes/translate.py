from fastapi import APIRouter, Request , HTTPException
import logging

from app.middleware.rate_limit import limiter
from app.config import get_settings
from app.translator import translator_instance
from app.models import TranslationRequest, TranslationResponse, HealthResponse, ErrorResponse

logger = logging.getLogger("translate_route")
settings = get_settings()

router = APIRouter()

@router.post("/translate", response_model=TranslationResponse)
@limiter.limit(settings.rate_limit)
async def translate(request: Request, payload: TranslationRequest):
    """ Traduit un texte du francais vers l'ewe
    -request list l'ip de lutilisateur"""
    if not translator_instance.is_ready():
        raise HTTPException(status_code=503,detail="Le service de traduction n'est pas encore disponible")

    try:
        translated=translator_instance.translate(payload.text)
    except Exception:
        logger.exception|("Erreur pendant la traduction")
        raise HTTPException(status_code=500, detail="une erreur interne est survenue pendant la traduction")

    return TranslationResponse(
        source_text = payload.text,
        translated_text = translated,
    )
