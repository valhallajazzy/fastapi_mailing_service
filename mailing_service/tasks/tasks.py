import os
import time
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

celery = Celery(__name__,
                broker=os.getenv('CELERY_BROKER_URL'),
                backend=os.getenv('CELERY_RESULT_BACKEND'))


@celery.task
def create_task(a, b, c):
    time.sleep(a)
    return b+c
