from django.shortcuts import render
from rest_framework import generics
from .models import Outflow
from .serializers import OutflowSerializer


# Create your views here.


class OutflowListCreateAPIView(generics.ListCreateAPIView):
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer


class OutflowRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer