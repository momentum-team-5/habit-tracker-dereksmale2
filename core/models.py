from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Habit(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user")
    name = models.CharField(max_length=255)


class Record(models.Model):
    habit = models.ForeignKey(to=Habit, on_delete=models.CASCADE, related_name="habit")
    date_completed = models.DateField()