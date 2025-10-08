from typing import Optional

from pydantic import BaseModel


class PostSchemaBase(BaseModel):
       id: Optional[int] = None
       titulo: str
       descricao: str
       image: Optional[str] = None
       id_usuario: Optional[int] = None
           
       class Config: 
<<<<<<< HEAD
        orm_mode = True
=======
        orm_mode = True

class PostSchemaShow(BaseModel):
       titulo: str
       descricao: str
       image: Optional[str] = None
>>>>>>> 689446a (first commit)
