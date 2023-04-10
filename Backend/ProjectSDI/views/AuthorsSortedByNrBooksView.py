from rest_framework.views import APIView
from rest_framework import generics

from django.db.models import Count, Sum

from ..models import Author, Book, AuthorBook
from ..serializers import AuthorsSortedByNrBooksSerializer

class AuthorsSortedByNrBooksView(generics.ListAPIView):
    queryset = Author.objects.annotate(nrBooksWritten=Count('authorbook')).order_by('-nrBooksWritten')
    serializer_class = AuthorsSortedByNrBooksSerializer