from django.db import models
from .User import User
class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    rating = models.FloatField(default=0.0)
    class Meta:
        app_label = 'courses'