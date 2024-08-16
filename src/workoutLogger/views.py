from django.shortcuts import render, redirect
from account.models import Account
from workoutLogger.models import Exercise, Set
from django.forms import modelformset_factory
from workoutLogger.forms import ExerciseForm, SetForm
from django.contrib import messages
# Create your views here.

def workout_log_home(request):
    exercises = Exercise.objects.filter(user=request.user).prefetch_related('sets')

    if not exercises.exists():
        messages.info(request, 'No exercises found. Start by logging your first workout!')
    else:
        print(f'Exercises: {exercises}')  # For debugging in the console

    context = {
        'exercises': exercises,
    }
    return render(request, "workoutLogger/workout_log_home.html", context)

def create_workout_log(request):
    ExerciseFormSet = modelformset_factory(Set, form=SetForm, extra=1)  # Allow for adding multiple sets
    if request.method == 'POST':
        exercise_form = ExerciseForm(request.POST)
        formset = ExerciseFormSet(request.POST)

        if exercise_form.is_valid() and formset.is_valid():
            exercise = exercise_form.save(commit=False)
            exercise.user = request.user  # Set the user to the currently logged-in user
            exercise.save()
            sets = formset.save(commit=False)
            for set_obj in sets:
                set_obj.exercises = exercise
                set_obj.save()
            messages.success(request, 'Workout saved successfully!')
            return redirect('workoutLogger:workoutLogHome')
        else:
            messages.error(request, 'There was an error saving your workout. Please try again.')
    else:
        exercise_form = ExerciseForm()
        formset = ExerciseFormSet(queryset=Set.objects.none())

    context = {
        'exercise_form': exercise_form,
        'formset': formset,
    }
    return render(request, 'workoutLogger/create_workout_log.html', context)

def exercise_view(request):
    return render(request, "workoutLogger/exercises.html", {})