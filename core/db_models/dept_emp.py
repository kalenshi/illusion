from django.db import models

from core.db_models.department import Department


class DeptEmp(models.Model):
    emp_no = models.OneToOneField(
        'Employee',
        models.DO_NOTHING,
        db_column='emp_no',
        primary_key=True
    )
    dept_no = models.ForeignKey(
        Department,
        models.DO_NOTHING,
        db_column='dept_no'
    )
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        app_label = "core"
        db_table = 'dept_emp'
        unique_together = (('emp_no', 'dept_no'),)
