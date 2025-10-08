from fastapi import APIRouter, status, Depends, HTTPException

from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.deps import get_session, get_current_user
from models.post_model import PostModel
from schemas.post_schema import PostSchemaShow



router = APIRouter()



router.get('/', status_code=status.HTTP_200_OK, response_model=List[PostSchemaShow])
async def get_posts(posts: PostModel, db: AsyncSession = Depends(get_session)):
       async with db as session:
              query = select(PostModel)
              result = await session.execute(query)
              posts: List[PostSchemaShow] = result.scalars().all()

              if posts:
                     return posts
              
              else:
                     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)