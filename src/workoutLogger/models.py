from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from account.models import Account
from datetime import date

def upload_location(instance, filename):

    file_path = 'workouts/{user_id}/{title}-{filename}'.format(
        user_id = str(instance.user.id),
        title = str(instance.title),
        filename=filename
    )
    return file_path

class presetExercise(models.Model):
    name                    = models.CharField(max_length=255, unique=True)
    description             = models.TextField(blank=True)
    slug                    = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.name

class Workout(models.Model):
    user                    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title                   = models.CharField(max_length=255)
    date                    = models.DateField(auto_now_add=True)
    slug                    = models.SlugField(blank=True, unique=True)
    image                   = models.ImageField(upload_to=upload_location, null=True, blank=True)
    
    def __str__(self):
        return f"{self.title} ({self.date})"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            if not self.date:
                self.date = date.today()
            date_str = self.date.strftime("%Y-%m-%d")
            self.slug = slugify(f"{self.title}-{date_str}")
        super().save(*args, **kwargs)
    
class Exercise(models.Model):
    workout                 = models.ForeignKey(Workout, related_name="exercises", on_delete=models.CASCADE)
    preset_exercise         = models.ForeignKey(presetExercise, related_name='instances', on_delete=models.CASCADE)
    order                   = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.name} (Order: {self.order})"

class Set(models.Model):
    exercises               = models.ForeignKey(Exercise, related_name='sets', on_delete=models.CASCADE)
    previous_weight         = models.IntegerField(null=True, blank=True)
    previous_reps           = models.IntegerField(null=True, blank=True)
    weight                  = models.IntegerField()
    reps                    = models.IntegerField()
    
    def __str__(self):
        return f"Set {self.pk}: {self.weight} lbs x {self.reps} reps"

@receiver(post_delete, sender=Workout)
def submission_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)

# @receiver(pre_save, sender=Workout)
# def pre_save_workout_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(instance.title + "-" + str(instance.date))
        
# pre_save.connect(pre_save_workout_receiver, sender=Workout)
        
@receiver(pre_save, sender=presetExercise)
def pre_save_preset_exercise_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)

pre_save.connect(pre_save_preset_exercise_receiver, sender=presetExercise)
