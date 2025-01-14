import os

from django.contrib import admin

from workoutApp.models import Workout, Exercise, Goals

import requests


# Register your models here.

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['duration', 'calories_burn', 'workout_date']
    list_editable = ['duration']
    search_fields = ['workout_types', 'workout_date']
    list_display_links = None

    @admin.display(ordering='workout_types', description='Workout Type')
    def workout_status(self, workout_types):
        if workout_types is None:
            return 'Please select a workout type'
        return workout_types

    @admin.display(ordering='calories_burn', description='Calories Burn')
    def total_calories_burn_in_a_week(self, calories_burn):
        activity = 'skiing'
        api_url = 'https://api.api-ninjas.com/v1/caloriesburned?activity={}'.format(activity)
        headers = {
            'X-api-key': os.getenv('API_KEY')
        }
        response = requests.get(api_url, headers=headers)
        if response.status_code == requests.codes.ok:
            print(response.text)
        else:
            print("Error:", response.status_code, response.text)


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['exercise_type']
    search_fields = ['exercise_type']

    @admin.display(ordering='exercise_type', description='Exercise Type')
    def select_exercise_status(self, exercise_type):
        if exercise_type is None:
            return 'Please select exercise type'
        return exercise_type


@admin.register(Goals)
class GoalsAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'target_date']
    search_fields = ['description', 'target_date']
