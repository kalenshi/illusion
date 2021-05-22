from django.db import models

from core.db_models.employee import Employee


class Titles(models.Model):
    emp_no = models.OneToOneField(
        Employee,
        models.DO_NOTHING,
        db_column='emp_no',
        primary_key=True
    )
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)

    class Meta:
        app_label = "core"
        db_table = 'titles'
        unique_together = (
            ('emp_no', 'title', 'from_date'),
        )

    def __str__(self):
        """"String Representation of titles"""
        return f"{self.emp_no}: {self.title}"
