from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from .basemodel import BaseModel

class Users(BaseModel, SQLAlchemyBaseUserTableUUID):
    pass

