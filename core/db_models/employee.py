from django.db import models


class Employee(models.Model):
    emp_no = models.AutoField(primary_key=True)
    birth_date = models.DateField()
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=16)
    gender = models.CharField(max_length=1)
    hire_date = models.DateField()

    class Meta:
        app_label = "core"
        db_table = 'employee'

    def __str__(self):
        """String Representation of Employee"""
        return f"{self.first_name}, {self.last_name}"
