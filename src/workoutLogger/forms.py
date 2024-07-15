# forms.py
from django import forms
from django.forms import inlineformset_factory
from .models import Set, Exercise, Workout

class SetForm(forms.ModelForm):
    class Meta:
        model = Set
        fields = ['weight', 'reps']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['preset_exercise', 'order']
        widgets = {
            'preset_exercise': forms.Select(attrs={'class' : 'preset-exercise'}),
        }
        
class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['title', 'image']

SetFormSet = inlineformset_factory(Exercise, Set, form=SetForm, extra=1, can_delete=True)
ExerciseFormSet = inlineformset_factory(Workout, Exercise, form=ExerciseForm, extra=1, can_delete=True)
        
