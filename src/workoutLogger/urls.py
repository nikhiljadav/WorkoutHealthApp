from django.urls import path
from workoutLogger.views import(
    create_workout_log,
    workout_log_home,
    exercise_view,
)

app_name = 'workoutLogger'

urlpatterns = [
    path('createLog/', create_workout_log, name="createLog"),
    path('home/', workout_log_home, name="workoutLogHome"),
    path('exercises/', exercise_view, name="exercisesHome")
]