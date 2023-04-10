from rest_framework.views import APIView
from rest_framework import generics

from ..models import Publisher
from ..serializers import PublisherSerializer
from ..serializers import OnePublisherSerializer


class PublisherList(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class PublisherDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = OnePublisherSerializer