from django.urls import path
from . import views


urlpatterns = [
    path('suppliers/', views.SupplierListCreateAPIView.as_view(), name='supplier-list-create'),
    path('suppliers/<int:pk>/', views.SupplierRetrieveUpdateDestroyAPIView.as_view(), name='supplier-retrieve-update-destroy'),
]