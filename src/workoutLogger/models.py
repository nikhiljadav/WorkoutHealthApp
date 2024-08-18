from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from account.models import Account
from datetime import date
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Exercise(models.Model):
    TYPE_CHOICES = [('compound', "Compound"), ('isolation', 'Isolation'),]
    name                    = models.CharField(max_length=100,  null=True, blank=True)
    type                    = models.CharField(max_length=10, choices=TYPE_CHOICES)
    upperRange              = models.IntegerField(null=True, blank=True)
    lowerRange              = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='exercises', null=True, blank=True) 
    recWeight               = models.IntegerField(default=0, null=True, blank=True)    
    def __str__(self):
        return f'{self.name} ({self.get_type_display()}) - Rep Range: {self.lowerRange} - {self.upperRange}'

class Set(models.Model):
    exercises               = models.ForeignKey(Exercise, related_name='sets', on_delete=models.CASCADE)
    weight                  = models.IntegerField()
    reps                    = models.IntegerField()
    RPE                     = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], null=True, blank=True)
    
    def __str__(self):
        return f"Set {self.pk}: {self.weight} lbs x {self.reps} reps at {self.RPE}"
