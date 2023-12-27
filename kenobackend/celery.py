from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_channels_example.settings')

app = Celery('django_channels_example_celery')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """
    First Start Task
    :param sender:
    :param kwargs:
    :return:
    """
    sender.add_periodic_task(1.0, first_task.s(), name='first_task')


@app.task
def first_task():
    """
    Periodic Task
    :return:
    """
    print('first_task')

    from randomgenerator.consumers import send_msg

    send_msg()
