from django.db import models
from robots.models import  Robot


class Customer(models.Model):
    email = models.CharField(max_length=255,blank=False, null=False)

class RobotAvailability(models.Model):
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
    available = models.BooleanField(default=False)
    queued_for_notification = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)

class RobotRequest(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)