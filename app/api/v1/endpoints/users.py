from fastapi import Depends, APIRouter

# from app.db import Use
from app.schemas.users import UserCreate, UserRead, UserUpdate
from app.api.deps import auth_backend, current_active_user, fastapi_users

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


# @app.get("/authenticated-route")
# async def authenticated_route(user: User = Depends(current_active_user)):
#     return {"message": f"Hello {user.email}!"}
