# Generated by Django 4.0.4 on 2022-05-19 10:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('due_dates', '0002_due_description_due_dueon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='due',
            name='dueon',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
