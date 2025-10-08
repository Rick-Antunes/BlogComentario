from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router
<<<<<<< HEAD
=======
from models.__all_models import *

from sqlalchemy.orm import configure_mappers

configure_mappers()
>>>>>>> 689446a (first commit)


app = FastAPI(title="Blog - Compartilhe sua opinião!")
app.include_router(api_router, prefix=settings.API_V1)

if __name__=="__main__":
       import uvicorn

       uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)