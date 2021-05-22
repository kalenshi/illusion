from rest_framework import serializers

from core.db_models.employee import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """Used to serialize/deserialize Employee model"""

    class Meta:
        model = Employee
        fields = [
            "emp_no",
            "birth_date",
            "first_name",
            "last_name",
            "gender",
            "hire_date"
        ]
