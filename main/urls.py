from django.urls import path

from main.apps import MainConfig
from main.views import NetworkNodeCreateAPIView, NetworkNodeUpdateAPIView, NetworkNodeRetrieveAPIView, \
    NetworkNodeListAPIView, NetworkNodeDestroyAPIView

app_name = MainConfig.name

urlpatterns = [
    path('create-networknode/', NetworkNodeCreateAPIView.as_view(), name='create_networknode'),
    path('update-networknode/<int:pk>/', NetworkNodeUpdateAPIView.as_view(), name='update_networknode'),
    path('retrieve-networknode/<int:pk>/', NetworkNodeRetrieveAPIView.as_view(), name='retrieve_networknode'),
    path('networknodes/', NetworkNodeListAPIView.as_view(), name='networknodes_list'),
    path('destroy-networknode/<int:pk>/', NetworkNodeDestroyAPIView.as_view(), name='destroy-networknode')
]