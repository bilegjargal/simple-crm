from django.core import management

from simple_crm import celery_app


@celery_app.task
def clearsessions():
    management.call_command('clearsessions')
