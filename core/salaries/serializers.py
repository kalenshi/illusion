from datetime import datetime

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

    def create(self, validated_data):
        """Override the create method"""
        Salaries.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Override default update for custom updating"""
        pass

    def validate(self, data):
        """Validate incoming data"""

        if data["from_date"] > data["to_date"]:
            raise serializers.ValidationError("Start date should be valid")

        return data
