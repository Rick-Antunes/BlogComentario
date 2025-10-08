from typing import Optional, List

from pydantic import BaseModel, EmailStr

from schemas.post_schema import PostSchemaBase

class UsuarioSchemaBase(BaseModel):
<<<<<<< HEAD
=======


>>>>>>> 689446a (first commit)
    id: Optional[int] = None
    nome: Optional[str] = None
    email: EmailStr
    admin: bool = False     
               
    class Config: 
        rm_mode = True


class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str


class UsuarioSchemaPost(UsuarioSchemaBase):
    post: Optional[List[PostSchemaBase]] = None


class UsuarioSchemaUp(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    senha: Optional[str] = None
