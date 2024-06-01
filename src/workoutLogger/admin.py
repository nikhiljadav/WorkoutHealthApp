from django.contrib import admin

from workoutLogger.models import Workout, presetExercise, Exercise, Set

admin.site.register(Workout)
admin.site.register(presetExercise)
admin.site.register(Exercise)
admin.site.register(Set)

# Register your models here.
