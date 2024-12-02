from celery import shared_task


@shared_task
def ss_debug(x, y):
    x + y