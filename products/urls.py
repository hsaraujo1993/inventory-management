from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),
]