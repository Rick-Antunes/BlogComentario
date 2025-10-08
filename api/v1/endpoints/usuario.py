from fastapi import APIRouter, HTTPException, status, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from schemas.usuario_schema import UsuarioSchemaBase, UsuarioSchemaCreate, UsuarioSchemaPost, UsuarioSchemaUp
from core.deps import get_session, get_current_user
from core.auth import autenticar, criar_token_acesso
from models.usuario_model import UsuarioModel
<<<<<<< HEAD

=======
from core.security import gerar_hash_senha
>>>>>>> 689446a (first commit)

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError


router = APIRouter()


#SIGN UP, LOGIN E LOGADO
@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UsuarioSchemaBase)
async def post_usuario(usuario: UsuarioSchemaCreate, db: AsyncSession = Depends(get_session)):
<<<<<<< HEAD
       novo_usuario: UsuarioModel = UsuarioModel(nome=usuario.nome, email=usuario.email, senha=usuario.senha, admin=usuario.admin, )

       async with db as session:
              try:
                     db.add(novo_usuario)
                     await db.commit()
=======
       novo_usuario: UsuarioModel = UsuarioModel(nome=usuario.nome, email=usuario.email, senha=gerar_hash_senha(usuario.senha), admin=usuario.admin, )

       async with db as session:
              try:
                     session.add(novo_usuario)
                     await session.commit()
>>>>>>> 689446a (first commit)
                     return novo_usuario
              
              except IntegrityError:
                     HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Já existe um usuário com esse email")


@router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
       usuario = await autenticar(email=form_data.username, senha=form_data.password, db=db)

       if not usuario:
              raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Dados incorretos. ")
       
       else:
              return JSONResponse(content={"access_token": criar_token_acesso(sub=usuario.id), "token_type": "bearer"}, status_code=status.HTTP_200_OK)
       

@router.get('/logado', response_model= UsuarioSchemaBase)
def get_logado(usuario_logado:UsuarioModel = Depends(get_current_user)):
       return usuario_logado



#######################
<<<<<<< HEAD

=======
# GET, PUT, DELETE USUARIO
>>>>>>> 689446a (first commit)


@router.get('/{usuario_id}', status_code=status.HTTP_200_OK, response_model=UsuarioSchemaBase)
async def get_usuario(usuario_id: int, db: AsyncSession = Depends(get_session)):
       async with db as session:
              query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
              result = await session.execute(query)
              usuario: UsuarioSchemaBase = result.scalars().unique().one_or_none()

              if usuario:
                     return usuario
              
              else:
                     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário com este ID não encontrado")
              

@router.delete('/{usuario_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_usuario(usuario_id: int, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)):
       async with db as session:
              if usuario_id == usuario_logado.id:
                     query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
                     result = await session.execute(query)
                     usuario_del: UsuarioSchemaPost = result.scalars().unique().one_or_none()

                     if usuario_del:
<<<<<<< HEAD
                            session.delete(usuario_del)     
=======
                            await session.delete(usuario_del)     
>>>>>>> 689446a (first commit)
                            await session.commit()
                            return Response(status_code=status.HTTP_204_NO_CONTENT)

                     else:
                            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário com este ID não encontrado")
              else:
                     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Você não tem permissão")


@router.put('/{usuario_id}', status_code=status.HTTP_202_ACCEPTED, response_model=UsuarioSchemaBase)
async def put_usuario(usuario_id: int, usuario: UsuarioSchemaUp, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)):
       async with db as session:
              if usuario_id == usuario_logado.id:
                     query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
                     result = await session.execute(query)
                     usuario_up: UsuarioSchemaBase = result.scalars().unique().one_or_none()

                     if usuario_up:

                            if usuario.nome:
                                   usuario_up.nome = usuario.nome

                            if usuario.email:
                                   usuario_up.email = usuario.email

                            if usuario.senha:
                                   usuario_up.senha = usuario.senha

                            await session.commit()
                            return usuario_up

                     else:
                            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário com este ID não encontrado")
              else:
                     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Você não tem permissão")