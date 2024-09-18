from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import db_helper
from core.schemas.user import UserRead
from crud.users import get_all_users

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["users"]
)


@router.get("/", response_model=list[UserRead])
async def get_users(
        session: AsyncSession = Depends(db_helper.session_getter)
):
    users = await get_all_users(session=session)
    return users
