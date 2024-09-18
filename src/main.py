from contextlib import asynccontextmanager

from fastapi import FastAPI

import api
from core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(api.router)
