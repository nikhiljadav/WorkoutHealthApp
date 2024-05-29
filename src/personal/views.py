from django.shortcuts import render
from personal.models import Workout
from personal.models import Exercise
from personal.models import ExerciseLog
from django.shortcuts import render, get_object_or_404
from personal.forms import WorkoutSelectionForm
from account.models import Account


# Create your views here.

#homescreen view
def home_screen_view(request):
    
    context = {}

    accounts = Account.objects.all()
    context['accounts'] = accounts
    

    return render(request, "personal/home.html", context) 
    #already looking at templates