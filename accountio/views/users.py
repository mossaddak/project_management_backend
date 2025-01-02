from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny

from ..serializers.users import UserRegisterSerializer, UserListSerializer, UserLoginSerializer
from ..models import User


class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


class UserListView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserDetailsView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    lookup_field = "id"

class UserLoginView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
