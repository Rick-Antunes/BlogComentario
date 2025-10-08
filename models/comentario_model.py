from core.configs import settings

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class ComentarioModel(settings.DBBaseModel):
    __tablename__ = "comentarios"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    like: bool = Column(Boolean, nullable=True, default=None)
    descricao: str = Column(String, nullable=False)
    id_post: int = Column(Integer, ForeignKey("posts.id"))
    id_usuario: int = Column(Integer, ForeignKey("usuarios.id"))

    post = relationship(
        "PostModel",
        back_populates="comentarios",
        lazy="joined"
    )
