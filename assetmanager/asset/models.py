from django.db import models
from model_utils import Choices
from django.utils import timezone
from datetime import datetime, date

# Create your models here.


class Asset(models.Model):

    category_choice = Choices('SELECT', 'machinery',
                              'motor vehicle', 'computers', 'building', 'lands')

    departments_choice = Choices(
        'SELECT', 'finance', 'human resource', 'procurement', 'IT', 'marketing', 'production')

    name = models.CharField(max_length=200)
    serial_number = models.PositiveIntegerField()
    acquisition_date = models.DateField(default=timezone.now)
    timestamp = models.DateField(auto_now_add=True,auto_now=False,blank=False,null=True)
    departments = models.CharField(
        choices=departments_choice, default=departments_choice.SELECT, max_length=64)
    category = models.CharField(
        choices=category_choice, default=category_choice.SELECT, max_length=64)
    

    def __str__(self):
        return self.name 

    def get_id(self):
        return str(self.id)
class Appreciate(models.Model):
    name = models.ForeignKey(Asset,null=True, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    appreciation_rate = models.PositiveIntegerField(null=True)
    months = models.PositiveIntegerField(null=True)
   


    def __str__(self):
        return self.name

class Depreciate(models.Model):
    name = models.ForeignKey(Asset,null=True, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    depreciation_rate = models.PositiveIntegerField(null=True)
    months = models.PositiveIntegerField(null=True)
