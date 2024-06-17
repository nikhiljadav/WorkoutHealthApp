from django.shortcuts import render, redirect
from workoutLogger.forms import WorkoutForm, ExerciseForm, SetFormSet
from account.models import Account
from workoutLogger.models import Workout
# Create your views here.

def workout_log_home(request):
    context = {}
    workouts = Workout.objects.filter(request.USER)
    context['workouts'] = workouts
    return render(request, "workoutLogger/workout_log_home.html")

def create_workout_log(request):
    context = {}
    if request.method == "POST":
        workout_form = WorkoutForm(request.POST, request.FILES)
        exercise_form = ExerciseForm(request.POST)
        if workout_form.is_valid() and exercise_form.is_valid():
            workout = workout_form.save(commit=False)
            exercise = exercise_form.save(commit=False)
            workout.user = request.user
            workout.save()
            exercise.workout = workout
            exercise.save()
            
            set_formset = SetFormSet(request.POST, instance=exercise)
            if set_formset.is_valid():
                set_formset.save()
            return redirect('workoutLogger:workoutLogHome')
    else:
        workout_form = WorkoutForm()
        exercise_form = ExerciseForm()
        set_formset = SetFormSet()
    
    context['workout_form'] = workout_form
    context['exercise_form'] = exercise_form
    context['set_formset'] = set_formset
    # context = {}
    # workout_form = WorkoutForm()
    # exercise_form = ExerciseForm()
    # set_form = SetForm()
    # context['workout_form'] = workout_form
    # context['exercise_form'] = exercise_form
    # context['set_form'] = set_form
    
    
    
    return render(request, "workoutLogger/create_workout_log.html", context)

def exercise_view(request):
    return render(request, "workoutLogger/exercises.html", {})