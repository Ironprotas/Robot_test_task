from django.apps import AppConfig

import logging

class CustomersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customers'

    def ready(self):
        from R4C import apscheduler
        apscheduler.start()

        logger = logging.getLogger(__name__)
        logger.info('New started')


