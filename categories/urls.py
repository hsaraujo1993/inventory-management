from django.urls import path
from . import views



urlpatterns = [
    path('categories/', views.CategoryListCreateAPIView.as_view(), name='categories-list-create'),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view(), name='categories-retrieve-update-destroy'),
]