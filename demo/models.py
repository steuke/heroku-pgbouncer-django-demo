from django.db import models
from django.utils.timezone import now


class SomeItem(models.Model):
    date_created = models.DateTimeField(default=now)
