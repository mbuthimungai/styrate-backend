from dataclasses import dataclass
from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.orm import registry, Mapped, declared_attr
from app.utils.idgen import idgen
from datetime import datetime





class Base_:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class BaseModel(Base_):
    id: Mapped[str] = Column(primary_key=True, default=idgen)
    created_on: Mapped[datetime] = Column(DateTime(timezone=True), server_default=func.now())
    updated_on: Mapped[datetime] = Column(DateTime(timezone=True), onupdate=func.now())
