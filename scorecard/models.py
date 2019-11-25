from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core import validators




# Create your models here.

class Scorecard(models.Model):
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    played_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
    score = models.CharField(max_length=35,validators=[validators.validate_comma_separated_integer_list])
    card = []

    def save_sc(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.location
