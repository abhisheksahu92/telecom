from rest_framework import serializers
from .models import CustomerPlan
from datetime import datetime, timedelta

class PlanRenewalSerializer(serializers.Serializer):
    renewal_date = serializers.DateField()
    plan_status = serializers.ChoiceField(choices=['Active', 'Inactive'])

class CustomerPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPlan
        fields = '__all__'

    def create(self, validated_data):
        customer_id = validated_data['customer']
        plan = validated_data.get('plan')

        if CustomerPlan.objects.filter(customer=customer_id).exists():
            raise serializers.ValidationError({'msg':'Customer already exists.'})

        # Ensure that the existing_plan_name is filled from Plan model before saving
        if plan:
            validated_data['existing_plan_name'] = plan.name
            validated_data['renewal_date'] = datetime.now().date() + timedelta(days=plan.validity)
            validated_data['existing_plan_expiry'] = validated_data['renewal_date'] - timedelta(days=1)
            validated_data['plan_status'] = 'Active'
        return super().create(validated_data)

    def update(self, instance, validated_data):
        plan_id = validated_data.get('plan')
        if plan_id:
            instance.new_plan_name = plan_id.name
            instance.save()
        return instance