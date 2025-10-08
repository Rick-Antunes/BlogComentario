from core.configs import settings

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship



class UsuarioModel(settings.DBBaseModel):
    __tablename__ = "usuarios"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String, nullable=True)
    email: str = Column(String, nullable=False)
    senha: str = Column(String, nullable=False)
    admin: bool = Column(Boolean, default=False)
    
    posts = relationship(
        "PostModel",
        back_populates="autor",
        cascade="all, delete-orphan",
        uselist=True,
        lazy="joined"
    )

    
