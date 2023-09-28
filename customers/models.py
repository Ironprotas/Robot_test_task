from django.db import models
from robots.models import  Robot

class Customer(models.Model):
    email = models.CharField(max_length=255,blank=False, null=False)


class RobotAvailability(models.Model):
    robot = models.OneToOneField(Robot, on_delete=models.CASCADE, related_name='availability')
    available = models.BooleanField(default=True)

