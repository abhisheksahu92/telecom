from rest_framework import serializers
from .models import Customer
import re

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def validate(self, data):
        # Custom validation to check if all required fields are present
        required_fields = ['name', 'dob', 'email', 'adhar_number', 'assigned_mobile_number']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            raise serializers.ValidationError(f"Missing required fields: {', '.join(missing_fields)}")

        return data

    def validate_name(self, value):
        name = value
        if not name:
            raise serializers.ValidationError("Name field cannot be empty")
        return name

    def validate_dob(self, value):
        dob = value
        if not dob:
            raise serializers.ValidationError("Date of birth field cannot be empty")
        return dob

    def validate_email(self, value):
        email = value
        if not email:
            raise serializers.ValidationError("Email field cannot be empty")

        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            raise serializers.ValidationError("Invalid email format")

        return email

    def validate_adhar_number(self, value):
        adhar_number = value
        if not adhar_number:
            raise serializers.ValidationError("Adhar number field cannot be empty")
        return adhar_number

    def validate_assigned_mobile_number(self, value):
        assigned_mobile_number = value
        if not assigned_mobile_number:
            raise serializers.ValidationError("Assigned mobile number field cannot be empty")
        return assigned_mobile_number