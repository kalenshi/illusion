from django.db import models


class Department(models.Model):
    dept_no = models.CharField(primary_key=True, max_length=4)
    dept_name = models.CharField(unique=True, max_length=40)

    class Meta:
        app_label = "core"
        db_table = 'department'

    def __str__(self):
        """String representation of the Department model"""
        return f"{self.dept_no}: {self.dept_name}"
