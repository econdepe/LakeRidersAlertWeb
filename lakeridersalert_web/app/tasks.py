from celery import shared_task

from .scripts.alert.run import run_once_conditionally
from . import LOGIN_EMAIL, LOGIN_PASSWORD, BOT_TOKEN, CHAT_ID


@shared_task()
def crawl_and_alert():
    run_once_conditionally(
        email=LOGIN_EMAIL, password=LOGIN_PASSWORD, token=BOT_TOKEN, chat_id=CHAT_ID
    )
