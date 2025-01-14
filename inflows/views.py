from django.shortcuts import render
from rest_framework import generics
from .models import Inflow
from .serializers import InflowSerializer

# Create your views here.


class InflowListCreateAPIView(generics.ListCreateAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer


class InflowRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer