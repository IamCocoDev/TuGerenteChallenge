from django.urls import path
from .views import BillingDataView, BookingViews, ClientView

urlpatterns = [
    path('booking/', BookingViews.as_view()),
    path('client/', ClientView.as_view()),
    path('billingdata/', BillingDataView.as_view())
]