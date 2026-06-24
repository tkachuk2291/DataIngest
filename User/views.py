from rest_framework import viewsets
from User.models import CustomUser
from User.permissions import IsAdminRole
from User.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminRole]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer