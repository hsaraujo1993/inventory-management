from django.urls import path
from . import views


urlpatterns = [
    path('brands/', views.BrandListCreateAPIView.as_view(), name='brand-list-create'),
    path('brands/<int:pk>/', views.BrandRetrieveUpdateDestroyAPIView.as_view(), name='brand-retrieve-update-destroy'),
]