from rest_framework import serializers
from .models import Plan
from datetime import timedelta,datetime
from django.http import JsonResponse

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

    def validate(self, data):
        # Ensure all fields are present in the request data
        required_fields = set(['name', 'cost', 'validity', 'status'])
        request_fields = set(data.keys())
        missing_fields = required_fields - request_fields
        if missing_fields:
            raise serializers.ValidationError(
                f"The following fields are missing in the request data: {', '.join(missing_fields)}"
            )

        # Ensure no fields have empty values
        for field, value in data.items():
            if not value:
                raise serializers.ValidationError(f"The field '{field}' cannot be empty")

        return data