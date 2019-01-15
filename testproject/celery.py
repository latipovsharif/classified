import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
 'testproject.settings')

app = Celery('testproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

CELERY_BEAT_SCHEDULE = {
    'view-counter-main-thread': {
        'task': 'classifield.tasks.count_classified_views',
        'schedule': 30.0, #  Каждые 30 сек
    }
}