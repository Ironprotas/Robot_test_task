from django.db import models


class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=False, null=False)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)
    quantity = models.CharField(max_length=4, blank=True, null=True)
