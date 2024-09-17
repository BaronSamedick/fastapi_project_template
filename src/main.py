from fastapi import FastAPI

import api
from core.config import settings

app = FastAPI()
app.include_router(api.router, prefix=settings.api.prefix)
