from django.db import models


class User(models.Model):
    id = models.CharField(
        max_length=100, primary_key=True)
    real_name = models.CharField(
        max_length=150)
    time_zone = models.CharField(
        max_length=200)


class UserActivityPeriod(models.Model):
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
