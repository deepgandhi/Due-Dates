from django.db import models
from django.utils import timezone

# Create your models here.
class Act(models.Model):
    actname=models.CharField(max_length=255)
    
class Due_Date_Types(models.Model):
    date_type=models.CharField(max_length=255)

class Compliance(models.Model):
    act=models.ForeignKey(Act, on_delete=models.CASCADE)
    due_date_type=models.ForeignKey(Due_Date_Types, on_delete=models.CASCADE)
    comp_name=models.CharField(max_length=255)

class Relevant_Period(models.Model):
    Month=models.IntegerChoices("month","January February March April May June July August September October November December")
    start_month=models.IntegerField(choices=Month.choices)
    start_year=models.IntegerField()
    end_month=models.IntegerField(choices=Month.choices)
    end_year=models.IntegerField()

class Due(models.Model):
    comp=models.ForeignKey(Compliance, on_delete=models.CASCADE)
    relevant_period=models.ForeignKey(Relevant_Period, on_delete=models.CASCADE)
    description=models.TextField(default="")
    dueon=models.DateField(default=timezone.now)
    