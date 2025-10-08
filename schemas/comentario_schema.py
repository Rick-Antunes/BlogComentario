from typing import Optional

from pydantic import BaseModel


class ComentarioBaseSchema(BaseModel):
    id: Optional[int] = None
    descricao: str
    estrelas: int 
    id_post: Optional[int] = None
    
    class Config: 
        orm_mode = True