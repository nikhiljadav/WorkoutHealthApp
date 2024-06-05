# forms.py
from django import forms
from .models import Set, Exercise

class SetForm(forms.ModelForm):
    class Meta:
        model = Set
        fields = ['weight', 'reps']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['preset_exercise']
