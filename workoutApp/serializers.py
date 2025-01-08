from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from workoutApp.models import Workout, Goals, Exercise, CustomUser


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ['first_name', 'last_name', 'age', 'gender', 'weight', 'height', 'email', 'password']


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'


class GoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goals
        fields = '__all__'


class ExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'





