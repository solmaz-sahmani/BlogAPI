import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.broker_url = 'redis://127.0.0.1:6379/0'

app.conf.broker_transport_options = {'visibility_timeout': 3600}  # 1 hour.

app.conf.result_backend = 'redis://127.0.0.1:6379/1'

app.conf.result_backend_transport_options = {
    'global_keyprefix': 'celery_',
    'retry_policy': {
       'timeout': 5.0
    },
    'result_chord_ordered': True    # or False
}
