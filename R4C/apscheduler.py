from apscheduler.schedulers.background import BackgroundScheduler
import logging
from customers.task import chek_Robot
from datetime import datetime


def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(chek_Robot, 'interval', seconds=600)
	scheduler.start()


logger = logging.getLogger(__name__)
logger.info('Scheduler has been started')
scheduler_initialized = True
