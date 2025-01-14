from django.urls import path
from . import views


urlpatterns = [
    path('outflows/', views.OutflowListCreateAPIView.as_view(), name='outflow-list-create'),
    path('outflows/<int:pk>/', views.OutflowRetrieveUpdateDestroyAPIView.as_view(), name='outflow-retrieve-update-destroy'),
]