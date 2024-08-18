from django import forms
from .models import Exercise, Set

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'type', 'lowerRange', 'upperRange']

class SetForm(forms.ModelForm):
    class Meta:
        model = Set
        fields = ['weight', 'reps', 'RPE']
