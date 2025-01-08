from django.contrib.auth.models import AbstractUser
from django.db import models

#
# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    email = models.EmailField(unique=True)


class WorkoutType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


WORKOUT_TYPES = [
    'Squats',
    'Step Ups',
    'Lunges',
    'Push Ups',
    'Wall Sits',
    'Dips',
]


class ExerciseType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


EXERCISE_TYPES = [
        'Squats',
        'Step Ups',
        'Lunges',
        'Push Ups',
    ]


class Exercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exerciseType = models.CharField(max_length=100, choices=EXERCISE_TYPES)


class Workout(models.Model):
    workout_type = models.CharField(max_length=100, choices=WORKOUT_TYPES)
    duration = models.DurationField()
    calories_burn = models.IntegerField()
    workout_date = models.DateTimeField()
