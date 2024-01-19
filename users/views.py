from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.permissions import IsAdmin
from users.serializers import UserSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]

    def perform_create(self, serializer):
        new_user = serializer.save()
        password = new_user.password
        new_user.set_password(password)
        new_user.save()

    def perform_update(self, serializer):
        updated_user = serializer.save()
        password = updated_user.password
        updated_user.set_password(password)
        updated_user.save()
