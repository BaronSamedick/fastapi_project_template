from fastapi import APIRouter

from . import users
from core.config import settings

router = APIRouter(
    prefix=settings.api.v1.prefix
)

router.include_router(users.router)
