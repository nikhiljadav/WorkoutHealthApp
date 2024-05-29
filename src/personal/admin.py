from django.contrib import admin
from personal.models import Workout
from personal.models import Exercise
from personal.models import ExerciseLog
from personal.models import Food

# Register your models here.
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(Food)
admin.site.register(ExerciseLog)