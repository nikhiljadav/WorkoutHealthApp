# Generated by Django 4.2.11 on 2024-07-29 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('compound', 'Compound'), ('isolation', 'Isolation')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('exercises', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sets', to='workoutLogger.exercise')),
            ],
        ),
    ]
