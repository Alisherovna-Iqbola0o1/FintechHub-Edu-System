from django.urls import path
from .views import PaymentListCreateAPIView

urlpatterns = [
    path('payment/', PaymentListCreateAPIView.as_view()),
    path('payment/<int:pk>/', PaymentListCreateAPIView.as_view()),
]