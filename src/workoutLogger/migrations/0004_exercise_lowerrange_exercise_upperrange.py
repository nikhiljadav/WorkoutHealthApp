# Generated by Django 4.2.11 on 2024-08-18 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workoutLogger', '0003_alter_exercise_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='lowerRange',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='upperRange',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
