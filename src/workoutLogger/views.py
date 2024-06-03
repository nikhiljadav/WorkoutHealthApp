from django.shortcuts import render

# Create your views here.

def workout_log_home(request):
    return render(request, "workoutLogger/workout_log_home.html")

def create_workout_log(request):
    return render(request, "workoutLogger/create_workout_log.html", {})

def exercise_view(request):
    return render(request, "workoutLogger/exercises.html", {})