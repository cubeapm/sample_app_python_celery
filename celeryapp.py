from celery import Celery
import logging

celery_app = Celery("my_celery_project")
celery_app.config_from_object(dict(
            broker_url="redis://redis",
            result_backend="redis://redis",
            task_ignore_result=True,
        ))
# celery_app.set_default()


@celery_app.task(bind=True, name="my-task")
def my_task(self, message):
    logging.info("task started")
    logging.info(message)
