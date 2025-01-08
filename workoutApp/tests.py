from django.test import TestCase

# Create your tests here.

class TestWorkoutApp(TestCase):
    def test_workout_app(self):

        response = self.client.get('/workout')

        assert response.POST.get('workout') == 'workout'


