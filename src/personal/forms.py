from django import forms
from .models import Workout

class WorkoutSelectionForm(forms.Form):
    workout = forms.ModelChoiceField(queryset=Workout.objects.all(), label="Select Workout")