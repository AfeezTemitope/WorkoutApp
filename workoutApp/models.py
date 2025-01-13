import random

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    email = models.EmailField(unique=True)


    def __str__(self):
        return self.username

    # def generate_otp(self):
    #     """generate a 6-digit OTP code"""
    #     otp = random.randint(100000, 999999)
    #     self.otp = str(otp)
    #     self.save()
    #     return self.otp


# Define the available workout types
class WorkoutType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    WORKOUT_TYPES = [
        ('squats', 'Squats'),
        ('step_ups', 'Step Ups'),
        ('lunges', 'Lunges'),
        ('push_ups', 'Push Ups'),
        ('wall_sits', 'Wall Sits'),
        ('dips', 'Dips'),
    ]
    workout_types = models.CharField(max_length=20, choices=WORKOUT_TYPES)

    def __str__(self):
        return self.name


# Define different exercise types
class ExerciseType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    EXERCISE_TYPES = [
        ('squats', 'Squats'),
        ('step_ups', 'Step Ups'),
        ('lunges', 'Lunges'),
        ('push_ups', 'Push Ups'),
    ]
    exercise_types = models.CharField(max_length=10, choices=EXERCISE_TYPES)

    def __str__(self):
        return self.name


# Represents an individual exercise performed by the user
class Exercise(models.Model):
    user = models.ForeignKey('workoutApp.CustomUser', on_delete=models.CASCADE, related_name='exercises')
    exercise_type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE, related_name='exercises')

    def __str__(self):
        return f'{self.user.name} - {self.exercise_type.name}'


# Represents a workout session performed by the user
class Workout(models.Model):
    user = models.ForeignKey('workoutApp.CustomUser', on_delete=models.CASCADE,
                             related_name='workouts')  # Added ForeignKey to User
    workout_type = models.ForeignKey(WorkoutType, on_delete=models.CASCADE, related_name='workouts')
    duration = models.DurationField()
    calories_burn = models.IntegerField()
    workout_date = models.DateTimeField()

    def __str__(self):
        return f'{self.user.name} - {self.workout_type.name} ({self.workout_date})'


# Represents the user's fitness goals
class Goals(models.Model):
    user = models.ForeignKey('workoutApp.CustomUser', on_delete=models.CASCADE, related_name='goals')
    description = models.CharField(max_length=255)
    target_date = models.DateField()

    def __str__(self):
        return f"{self.user.name}'s goal: {self.description}"
