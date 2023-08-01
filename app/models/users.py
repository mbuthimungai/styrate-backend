from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from .basemodel import BaseModel, Base_

class Users(Base_, SQLAlchemyBaseUserTableUUID):
    pass

