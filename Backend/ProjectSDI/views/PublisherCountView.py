from rest_framework.views import APIView
from rest_framework import generics

from ..models import Publisher, Book
from ..serializers import PublisherNrBooksSerializer

from django.db.models import Count, Sum

#display all the publishers based on the number of books published, field for number of books
class PublisherCountView(generics.ListAPIView):
    queryset = Publisher.objects.annotate(nrBooksPublished=Count('book')).order_by('-nrBooksPublished')
    serializer_class = PublisherNrBooksSerializer