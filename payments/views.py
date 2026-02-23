from rest_framework.generics import ListCreateAPIView
from .models import Payment
from .serializers import PaymentSerializer
# Create your views here.

class PaymentListCreateAPIView(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer