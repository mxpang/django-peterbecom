from django.db import models
from django.utils import timezone


class Measurement(models.Model):
    url = models.URLField()
    user_agent = models.CharField(max_length=250)
    driver = models.CharField(max_length=250, blank=True, null=True)
    xhr_median = models.FloatField()
    local_median = models.FloatField()
    plain_localstorage = models.BooleanField(default=False)
    iterations = models.PositiveIntegerField()
    add_date = models.DateTimeField(default=timezone.now)
