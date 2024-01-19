from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from main.models import NetworkNode
from main.paginators import CustomPaginator
from main.permissions import IsActive
from main.serializers import NetworkNodeSerializerCreate, NetworkNodeSerializerUpdate, \
    NetworkNodeSerializerListRetrieve, ProductSerializer


# Create your views here.

class NetworkNodeCreateAPIView(generics.CreateAPIView):
    serializer_class = NetworkNodeSerializerCreate
    permission_classes = [IsAuthenticated, IsActive]


class NetworkNodeUpdateAPIView(generics.UpdateAPIView):
    """
    Помимо запрета на изменение долга (debt) также запрещены
    изменение поставщика (supplier), т.к. ему принадлежит долг,
    а также изменение категории (category), т.к. в реальной жизни для
    смены подобной категории создается новое юр. лицо
    с новыми реквизитами
    """
    serializer_class = NetworkNodeSerializerUpdate
    queryset = NetworkNode.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class NetworkNodeRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = NetworkNodeSerializerListRetrieve
    queryset = NetworkNode.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class NetworkNodeListAPIView(generics.ListAPIView):
    serializer_class = NetworkNodeSerializerListRetrieve
    queryset = NetworkNode.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country',)
    pagination_class = CustomPaginator
    permission_classes = [IsAuthenticated, IsActive]


class NetworkNodeDestroyAPIView(generics.DestroyAPIView):
    queryset = NetworkNode.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive]
