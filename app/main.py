import logging 
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.config import get_settings
from app.translator import translator_instance
from app.middleware.rate_limit import limiter
from app.routes.translate import router as translate_router 
from app.models import HealthResponse 
from  app.exceptions import (
    validation_exception_handler,
    rate_limit_exception_handler,
    unhandled_exception_handler,

)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("main")

settings = get_settings()
@asynccontextmanager
async def lifespan(app: FastAPI):
    # demarrage du modele une seul fois
    logger.info("demarrage de l'api et chargement du modele")
    translator_instance.load()
    yield
    # arret 
    logger.info("arret de l'api")

app = FastAPI(title = settings.api_title , lifespan=lifespan)

# Rate Limiting
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

#cORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_credentials = True,
    allow_methods =["*"],
    allow_headers = ["*"],
)

#gestion des erreurs 
app.add_exception_handler(RequestValidationError,validation_exception_handler)
app.add_exception_handler(RateLimitExceeded,rate_limit_exception_handler)
app.add_exception_handler(Exception , unhandled_exception_handler)

#Routes 
app.include_router(translate_router)

@app.get("/health",response_model=HealthResponse)
async def health():
    #endpoint pour monitoring et fontend
    return HealthResponse(
        staus="ok",
        model_loaded = translator_instance.is_ready(),
    )