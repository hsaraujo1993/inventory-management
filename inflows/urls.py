from django.urls import path
from . import views


urlpatterns = [
    path('inflows/', views.InflowListCreateAPIView.as_view(), name='inflow-list-create'),
    path('inflows/<int:pk>/', views.InflowRetrieveUpdateDestroyAPIView.as_view(), name='inflow-retrieve-update-destroy'),
]