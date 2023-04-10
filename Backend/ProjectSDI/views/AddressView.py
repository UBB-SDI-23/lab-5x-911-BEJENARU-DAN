from django.shortcuts import render
from ..models import Address
from ..serializers import AddressSerializer
from rest_framework.views import APIView
from rest_framework import generics

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer