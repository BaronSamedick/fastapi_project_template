from fastapi import APIRouter

from core.config import settings
from . import v1

router = APIRouter(prefix=settings.api.prefix)

router.include_router(v1.router)
