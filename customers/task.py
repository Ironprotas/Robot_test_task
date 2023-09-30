from .models import Robot, RobotRequest
from django.core.mail import send_mail
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore


import logging
from django.http import JsonResponse

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

def chek_Robot():
    logger = logging.getLogger(__name__)
    all_robots = RobotRequest.objects.all()
    if len(all_robots) == 0:
        return JsonResponse({'message': 'Robots not in queue'}, status=200)
    for robot in all_robots:
        model = robot.model
        version = robot.version
        get_robot = Robot.objects.filter(model=model, version=version).first()
        if get_robot:
            subject = 'Робот доступен'
            message = f'Добрый день!\nНедавно вы интересовались нашим роботом модели {robot.model}, версии {robot.version}.\n' \
                      f'Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами.\n'
            from_email = 'Ironprotas@ya.ru'
            recipient_list = [robot.customer.email]  # Получаем адрес электронной почты пользователя

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            robot.delete()
            logger.info('Robot Delete')
        else:
            logger.info('Robot no found')
            continue
    logger.info('Robot Ended')
    return JsonResponse({'message': 'Send email ended'}, status=200)
