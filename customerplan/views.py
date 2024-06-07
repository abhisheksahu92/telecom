from rest_framework import viewsets
from .models import CustomerPlan
from .serializers import CustomerPlanSerializer,PlanRenewalSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class CustomerPlanViewSet(viewsets.ModelViewSet):
    queryset = CustomerPlan.objects.all()
    serializer_class = CustomerPlanSerializer

class PlanRenewalView(APIView):
    def post(self, request, customer_plan_id):
        try:
            customer_plan = CustomerPlan.objects.get(id=customer_plan_id)
        except CustomerPlan.DoesNotExist:
            return Response({"error": "Customer plan not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PlanRenewalSerializer(data=request.data)
        if serializer.is_valid():
            renewal_date = serializer.validated_data['renewal_date']
            plan_status = serializer.validated_data['plan_status']

            # Update customer plan
            customer_plan.renewal_date = renewal_date
            customer_plan.plan_status = plan_status
            customer_plan.save()

            return Response({"success": "Plan renewed successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
