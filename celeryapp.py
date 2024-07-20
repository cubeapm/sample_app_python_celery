from celery import Celery
from celery.signals import worker_process_init
from tracing import init_tracing
import logging

from opentelemetry.instrumentation.celery import CeleryInstrumentor


@worker_process_init.connect(weak=False)
def init_celery_tracing(*args, **kwargs):
    init_tracing()
    CeleryInstrumentor().instrument()
    # Additional instrumentation can be enabled by
    # following the docs for respective instrumentations at
    # https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation


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
