from rest_framework.generics import ListCreateAPIView
from .models import User
from .serializers import UserSerializer
# Create your views here.

class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer