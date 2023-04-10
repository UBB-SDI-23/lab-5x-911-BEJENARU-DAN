from rest_framework.views import APIView
from rest_framework import generics

from ..models import AuthorBook

from ..serializers import AuthorBookSerializer

class AuthorBookList(generics.ListCreateAPIView):
    queryset = AuthorBook.objects.all()
    serializer_class = AuthorBookSerializer


class AuthorBookDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorBook.objects.all()
    serializer_class = AuthorBookSerializer