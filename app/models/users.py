from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from .basemodel import Base_


class Users(Base_, SQLAlchemyBaseUserTableUUID):
    pass

