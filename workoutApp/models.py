from datetime import timezone

from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField()
    age = models.IntegerField()
    Password = models.CharField(max_length=100)

class WorkoutType(models.Model):
    CHOICES = [
        ('Squats', 'Step Ups'),
        ('Lunges', 'Push Ups'),
        ('Wall Sits', 'Dips'),
    ]

class ExerciseType(models.Model):
    TYPES = [
        ('Squats', 'Step Ups'),
        ('Lunges', 'Push Ups'),
    ]

class Exercise(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    exerciseType = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)


class Workout(models.Model):
    id = models.IntegerField()
    workoutType = models.ForeignKey(WorkoutType, on_delete=models.CASCADE)
    duration = models.DateTimeField(datetime=timezone.max)
    caloriesBurn = models.IntegerField()
    workoutDate = models.DateTimeField()

class Goals(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    workoutId = models.ForeignKey(Workout, on_delete=models.CASCADE)

