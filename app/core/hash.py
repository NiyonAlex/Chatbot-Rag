from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:
    @staticmethod
    def verify_password(pwd, hashed):
        return pwd_context.verify(pwd, hashed)

    @staticmethod
    def get_hashed(pwd):
        return pwd_context.hash(pwd)
