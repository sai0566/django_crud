from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class employee(models.Model):
    emp_id=models.IntegerField(unique=True)
    emp_name=models.CharField(max_length=100)
    options=[('it','IT'),('hr','HR'),('manager','MANAGER'),('sales','SALES')]
    emp_dept=models.CharField(max_length=20,choices=options)
    valid=RegexValidator(r'[6-9][0-9]{9}',message='Valid number starts from 6-9')
    emp_mobile=models.CharField(max_length=10,validators=[valid])
    emp_salary=models.FloatField()

    def __str__(self):
        return self.emp_name
