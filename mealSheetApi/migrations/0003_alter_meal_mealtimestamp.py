# Generated by Django 4.0.3 on 2022-03-16 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealSheetApi', '0002_meal_mealtime_meal_mealtimestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='mealTimestamp',
            field=models.DateTimeField(),
        ),
    ]
