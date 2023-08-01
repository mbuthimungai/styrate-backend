from pydantic import BaseModel
from dotenv import load_dotenv
import os
from kombu import Queue
from functools import lru_cache
import secrets

load_dotenv()

# fetch the routes per task at runtime
def route_task(name, args, kwargs, options, task=None, **kw):
    if ":" in name:
        queue, _ = name.split(":")
        return {"queue": queue}
    return {"queue": "celery"}

class Settings(BaseModel):
    PROJECT_NAME: str = os.getenv("PROJECT_NAME")
    API_VERSION: str = "v1"
    API_V1_STR: str = f"/api/{API_VERSION}"
    ASYNC_DATABASE_URI: str = os.getenv("ASYNC_DATABASE_URI")
    SECRET_KEY: str = secrets.token_urlsafe(32)
    BACKEND_CORS_ORIGINS: list = [os.getenv("BACKEND_CORS_ORIGINS")]
    
settings = Settings()

class BaseConfigCelery:
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
    RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")
    CELERY_TASK_QUEUES: list = (
        # default queue
        Queue("celery"),
        # custom queue
        Queue("send_email"),
    )
    CELERY_TASK_ROUTES = (route_task,)
    
class DevelopmentCeleryConfig(BaseConfigCelery):
    pass

@lru_cache
def get_celery_settings():
    config_cls_dict = {
        "development": DevelopmentCeleryConfig,
    }
    config_name = os.environ.get("CELERY_CONFIG", "development")
    config_cls = config_cls_dict[config_name]
    return config_cls()

celery_settings = get_celery_settings()