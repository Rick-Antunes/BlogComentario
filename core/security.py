from passlib.context import CryptContext
<<<<<<< HEAD
=======
import bcrypt
>>>>>>> 689446a (first commit)

CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verificar_senha(senha: str, hash_senha: str) -> bool:
<<<<<<< HEAD
=======

>>>>>>> 689446a (first commit)
       
       #Função para verificar se a senha está correta, comparando o
       #Hash_senha que é a sua senha salva com a "senha" que é a informada pelo usuário.
       
<<<<<<< HEAD

=======
>>>>>>> 689446a (first commit)
       return CRIPTO.verify(senha, hash_senha)


def gerar_hash_senha(senha: str) -> str:
       #Função que gera e retorna o hash da senha

<<<<<<< HEAD
=======

>>>>>>> 689446a (first commit)
       return CRIPTO.hash(senha)