from fastapi import Request , status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from slowapi.errors import RateLimitExceeded
import logging 

logger = logging.getLogger("exceptions")

async def validation_exception_handler(request: Request , exc: RequestValidationError):
# Intercepte les differents erreur quon a creer et renvoie ca en json
  first_error = exc.errors()[0]
  message = first_error.get("msg","requete invalide")

  return JSONResponse(
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,
    content={"error": "validation_error" ,"detail":message},

  )

async def rate_limit_exception_handler(request: Request , exc: RateLimitExceeded):
  # Intercepte les differentes depassement de rate limit et met en format json
  return JSONResponse(
    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
    content={
      "error": "rate_limit_exceeded",
      "detail": "trop de requeste : Limites de 5 par minutes"
    },
  )

async def unhandled_exception_handler(request: Request , exc: Exception):
  # Tout les erreurs non prevu sont logue en interne et jamais devant l'utilisateur
  logger.exption("erreur non gerer")
  return JSONResponse(
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
    content={"error": "internal_error" ,"detail":"une erreur interne est survenue"}
  )