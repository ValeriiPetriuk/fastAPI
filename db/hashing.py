from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')


def bcrypt_hash(password: str):
    return pwd_cxt.hash(password)


def bcrypt_verify(hashed_password: str, plain_password: str):
    return pwd_cxt.verify(plain_password, hashed_password)