from fastapi import APIRouter
from app.api.v1.endpoints import users
from app.core.celery import create_celery

celery = create_celery()
api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])