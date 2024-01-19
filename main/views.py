from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from main.models import NetworkNode
from main.paginators import CustomPaginator
from main.serializers import NetworkNodeSerializerCreate, NetworkNodeSerializerUpdate, NetworkNodeSerializerListRetrieve


# Create your views here.

class NetworkNodeCreateAPIView(generics.CreateAPIView):
    serializer_class = NetworkNodeSerializerCreate


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


class NetworkNodeRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = NetworkNodeSerializerListRetrieve
    queryset = NetworkNode.objects.all()


class NetworkNodeListAPIView(generics.ListAPIView):
    serializer_class = NetworkNodeSerializerListRetrieve
    queryset = NetworkNode.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country',)
    pagination_class = CustomPaginator


class NetworkNodeDestroyAPIView(generics.DestroyAPIView):
    queryset = NetworkNode.objects.all()
