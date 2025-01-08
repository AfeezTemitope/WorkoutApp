from rest_framework import serializers

from workoutApp.models import User, Workout, Goals, Exercise


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout


class GoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goals


class ExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
