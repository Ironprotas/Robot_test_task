from django.db import models
<<<<<<< HEAD
from robots.models import  Robot
=======
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from robots.models import  Robot

>>>>>>> Task3

class Customer(models.Model):
    email = models.CharField(max_length=255,blank=False, null=False)

<<<<<<< HEAD

class RobotAvailability(models.Model):
    robot = models.OneToOneField(Robot, on_delete=models.CASCADE, related_name='availability')
    available = models.BooleanField(default=True)

=======
class RobotAvailability(models.Model):
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
    available = models.BooleanField(default=False)
    queued_for_notification = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)

    def notify_customer(self):
        if self.available and self.customer:
            subject = 'Робот доступен в наличии'
            message = render_to_string('availability_notification_email.html', {
                'robot_model': self.robot.model,
                'robot_version': self.robot.version,
            })
            plain_message = strip_tags(message)
            from_email = 'noreply@example.com'
            recipient_list = [self.customer.email]
            mail.send_mail(subject, plain_message, from_email, recipient_list)
>>>>>>> Task3
