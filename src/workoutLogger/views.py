from django.shortcuts import render, redirect
from workoutLogger.forms import WorkoutForm, ExerciseForm, SetForm
# Create your views here.

def workout_log_home(request):
    return render(request, "workoutLogger/workout_log_home.html")

def create_workout_log(request):
    context = {}
    workout_form = WorkoutForm()
    exercise_form = ExerciseForm()
    set_form = SetForm()
    context['workout_form'] = workout_form
    context['exercise_form'] = exercise_form
    context['set_form'] = set_form
    
    
    
    return render(request, "workoutLogger/create_workout_log.html", context)

def exercise_view(request):
    return render(request, "workoutLogger/exercises.html", {})