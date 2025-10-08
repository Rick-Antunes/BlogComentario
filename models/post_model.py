from core.configs import settings

from sqlalchemy import String, Integer, Column, ForeignKey

from sqlalchemy.orm import relationship



class PostModel(settings.DBBaseModel):
    __tablename__ = "posts"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String, nullable=False)
    descricao: str = Column(String, nullable=False)
    image: str = Column(String, nullable=True)
    id_usuario: int = Column(Integer, ForeignKey('usuarios.id'))

    autor = relationship(
        "UsuarioModel",
        back_populates="posts",
        lazy="joined"
    )

    comentarios = relationship(
        "ComentarioModel",
        back_populates="post",
        cascade="all, delete-orphan",
        uselist=True,
        lazy="joined"
    
    )