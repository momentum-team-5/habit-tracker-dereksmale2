from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Habit(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="habits")
    name = models.CharField(max_length=255)


class Record(models.Model):
    habit = models.ForeignKey(to=Habit, on_delete=models.CASCADE, related_name="records")
    record_response = models.CharField(max_length=255, null=True)
    date_completed = models.DateField()

    class Meta:
        unique_together = [
            'habit', 
            'date_completed',
        ]