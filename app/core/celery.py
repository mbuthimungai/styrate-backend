from celery import current_app as current_celery_app
from celery.result import AsyncResult
from celery import Celery
from app.core.settings import celery_settings


def create_celery():
    """
    Customize an existing Celery app by setting various configuration options.

    Configuration options include:
    - Serialization of tasks and results using 'pickle'.
    - Task tracking to report when tasks are started.
    - Accepting content in both 'pickle' and 'json' formats.
    - Expiring task results after 200 seconds.
    - Storing task results persistently.
    - Preventing the worker from sending task events to the message broker.
    - Prefetching one task at a time from the message broker.

    Returns:
    A modified Celery app with updated configuration options.
    """
    celery_app = current_celery_app
    celery_app.config_from_object(celery_settings, namespace='CELERY')
    celery_app.conf.update(task_track_started=True)
    celery_app.conf.update(task_serializer='json')
    celery_app.conf.update(result_serializer='json')
    celery_app.conf.update(accept_content=['json'])
    celery_app.conf.update(result_expires=200)
    celery_app.conf.update(result_persistent=True)
    celery_app.conf.update(worker_send_task_events=False)
    celery_app.conf.update(worker_prefetch_multiplier=1)
    return celery_app


def get_task_info(task_id):
    """
    return task info for the given task_id
    """
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return result
