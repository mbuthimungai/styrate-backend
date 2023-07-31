from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.settings import settings

engine = create_async_engine(
    settings.ASYNC_DATABASE_URI, 
)

SessionLocal = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)