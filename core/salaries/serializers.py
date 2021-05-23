from rest_framework import serializers

from core.db_models.salaries import Salaries


class SalariesSerializer(serializers.ModelSerializer):
    """Serializer class for the salaries model"""

    class Meta:
        model = Salaries
        fields = [
            "emp_no",
            "salary",
            "from_date",
            "to_date"
        ]
