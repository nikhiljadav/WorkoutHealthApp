from django.db import models
from django.utils.text import slugify
# Create your models here.

PRIORITY = [("h", "High"), ("m", "Medium"), ("l", "Low")]
INTENSITY = [("E", "Easy"), ("H", "Hard"), ("F", "Failure")]
BODYPARTS = [("C", "Chest"), ("L", "Legs"), ("A", "Arms"), ("B", "Back"), ("S", "Shoulders"), ("Co", "Core")] 

# class Question(models.Model):
#     title                   = models.CharField(max_length=60)
#     question                = models.TextField(max_length=400)
#     priority                = models.CharField(max_length=1, choices=PRIORITY)

#     #function -> if i query question object and print it, shows default field
#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name        = "The Question"
#         verbose_name_plural = "Peoples Question"

# class Workout(models.Model):                                                #class that stores the name of the workout and date of the workout
#     name                    = models.CharField(max_length=100)
#     date                    = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name        = "Workout"
#         verbose_name_plural = "Workouts"

# class Exercise(models.Model):                                              #overarching exercise class that stores the name of the exercise and body part of the exercise
#     name                    = models.CharField(max_length=100)
#     bodyPart                = models.CharField(max_length=2, choices=BODYPARTS)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name        = "Exercise"
#         verbose_name_plural = "Exercises"

# class ExerciseLog(models.Model):                                            #class for recording exercises, takes in exercise, ests, weight, reps, and workout it relates to
#     exercise                = models.ForeignKey(Exercise, on_delete=models.CASCADE)
#     set_number              = models.PositiveIntegerField()
#     weight                  = models.DecimalField(max_digits=5, decimal_places=2)
#     reps                    = models.PositiveIntegerField()
#     workout                 = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="exercise_logs")

# class Food(models.Model):
#     name                    = models.CharField(max_length=100)
#     calories                = models.IntegerField()  # per serving
#     proteins                = models.FloatField()    # grams per serving
#     carbs                   = models.FloatField()       # grams per serving
#     fats                    = models.FloatField()        # grams per serving
#     date                    = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         verbose_name        = "Food"
#         verbose_name_plural = "Foods"
