from django.db import models

from core.db_models.employee import Employee


class Salaries(models.Model):
    emp_no = models.OneToOneField(
        Employee,
        models.DO_NOTHING,
        db_column='emp_no',
        primary_key=True,
        related_name="employee"
    )
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        app_label = "core"
        db_table = "salaries"
        get_latest_by = "to_date"
        unique_together = (('emp_no', 'from_date'),)
