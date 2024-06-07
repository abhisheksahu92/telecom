from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerPlanViewSet,PlanRenewalView

router = DefaultRouter()
router.register(r'customer-plans', CustomerPlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('customer-plans/renew/<int:customer_plan_id>/', PlanRenewalView.as_view(), name='renew-customer-plan'),
]
