from django.shortcuts import render, redirect
from workoutLogger.forms import WorkoutForm, ExerciseFormSet, SetFormSet
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
    if request.method == 'POST':
        workout_form = WorkoutForm(request.POST, request.FILES)
        exercise_formset = ExerciseFormSet(request.POST, request.FILES)

        if workout_form.is_valid() and exercise_formset.is_valid():
            workout = workout_form.save(commit=False)
            workout.user = request.user
            workout.save()

            for exercise_form in exercise_formset:
                if exercise_form.is_valid():
                    exercise = exercise_form.save(commit=False)
                    exercise.workout = workout
                    exercise.save()

                    set_formset = SetFormSet(request.POST, instance=exercise)
                    if set_formset.is_valid():
                        set_formset.save()
                    else:
                        messages.error(request, "Error saving sets")
                        return redirect('workoutLogger:createLog')
            messages.success(request, "Workout logged successfully")
            return redirect('workoutLogger:workoutLogHome')
        else:
            messages.error(request, "Invalid data in workout or exercise form")
            return redirect('workoutLogger:createLog')
    else:
        workout_form = WorkoutForm()
        exercise_formset = ExerciseFormSet(queryset=Exercise.objects.none())

    context = {
        'workout_form': workout_form,
        'exercise_formset': exercise_formset,
        'set_formset': SetFormSet(),
    }
    return render(request, 'workoutLogger/create_workout_log.html', context)
    # context = {}
    # if request.method == "POST":
    #     workout_form = WorkoutForm(request.POST, request.FILES)
    #     exercise_form = ExerciseForm(request.POST)
    #     if workout_form.is_valid() and exercise_form.is_valid():
    #         workout = workout_form.save(commit=False)
    #         exercise = exercise_form.save(commit=False)
    #         workout.user = request.user                         #sets user for workout to the request's user
    #         workout.save()                                      #saves workout
    #         exercise.workout = workout                          #saves exercises workout field to current workout field
    #         exercise.save()
            
    #         set_formset = SetFormSet(request.POST, instance=exercise)   #set formset assigned to the exercise instance
    #         if set_formset.is_valid():
    #             set_formset.save()
                
    #             if Workout.objects.filter(id=workout.id).exists() and Exercise.objects.filter(id=exercise.id).exists():
    #                 messages.success(request, "W and E saved successfully")
    #             else:
    #                 messages.error(request, "error saving workout")
        
    #             return redirect('workoutLogger:workoutLogHome')
            
    #         else:
    #             messages.error(request, "Invalid data in set formset")
    #     else:
    #         messages.error(request, "invalid workout or exercise form data")
    # else:
    #     workout_form = WorkoutForm()
    #     exercise_form = ExerciseForm()
    #     set_formset = SetFormSet()
    
    # context['workout_form'] = workout_form
    # context['exercise_form'] = exercise_form
    # context['set_formset'] = set_formset
    
    # return render(request, "workoutLogger/create_workout_log.html", context)

def exercise_view(request):
    return render(request, "workoutLogger/exercises.html", {})