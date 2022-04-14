from django.apps import AppConfig
import os

class HealthappConfig(AppConfig):
    name = 'HealthApp'

    def ready(self):
        from . import jobs
        if os.environ.get('RUN_MAIN', None) != True:
            jobs.start_scheduler()