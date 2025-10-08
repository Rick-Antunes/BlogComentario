from core.configs import settings
from core.database import engine

<<<<<<< HEAD
async def create_tables():
=======
async def create_tables() -> None:
>>>>>>> 689446a (first commit)
       import models.__all_models

       async with engine.begin() as conn:
              await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
              await conn.run_sync(settings.DBBaseModel.metadata.create_all)
       
if __name__ == "__main__":
       import asyncio
       asyncio.run(create_tables())