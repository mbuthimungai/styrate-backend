from fastapi_users import schemas
from uuid import UUID

class UserRead(schemas.BaseUser[UUID]):
    pass

class UserCreate(schemas.BaseUserCreate):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    pass
