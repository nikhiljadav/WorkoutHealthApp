from django.shortcuts import render, redirect
from workoutLogger.forms import WorkoutForm, ExerciseForm, SetFormSet
from account.models import Account
from workoutLogger.models import Workout, Exercise
from django.contrib import messages
# Create your views here.

def workout_log_home(request):
    context = {}
    workouts = Workout.objects.filter(user=request.user)
    context['workouts'] = workouts
    return render(request, "workoutLogger/workout_log_home.html", context)

def create_workout_log(request):
    context = {}
    if request.method == "POST":
        workout_form = WorkoutForm(request.POST, request.FILES)
        exercise_form = ExerciseForm(request.POST)
        if workout_form.is_valid() and exercise_form.is_valid():
            workout = workout_form.save(commit=False)
            exercise = exercise_form.save(commit=False)
            workout.user = request.user                         #sets user for workout to the request's user
            workout.save()                                      #saves workout
            exercise.workout = workout                          #saves exercises workout field to current workout field
            exercise.save()
            
            set_formset = SetFormSet(request.POST, instance=exercise)   #set formset assigned to the exercise instance
            if set_formset.is_valid():
                set_formset.save()
                
                if Workout.objects.filter(id=workout.id).exists() and Exercise.objects.filter(id=exercise.id).exists():
                    messages.success(request, "W and E saved successfully")
                else:
                    messages.error(request, "error saving workout")
        
                return redirect('workoutLogger:workoutLogHome')
            
            else:
                messages.error(request, "Invalid data in set formset")
        else:
            messages.error(request, "invalid workout or exercise form data")
    else:
        workout_form = WorkoutForm()
        exercise_form = ExerciseForm()
        set_formset = SetFormSet()
    
    context['workout_form'] = workout_form
    context['exercise_form'] = exercise_form
    context['set_formset'] = set_formset
    
    return render(request, "workoutLogger/create_workout_log.html", context)

def exercise_view(request):
    return render(request, "workoutLogger/exercises.html", {})