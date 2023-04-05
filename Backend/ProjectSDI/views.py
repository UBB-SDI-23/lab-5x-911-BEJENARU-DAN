from django.shortcuts import render
from .models import Book, Author, Publisher, AuthorBook, Address
from .serializers import BookSerializer, AuthorSerializer, PublisherSerializer, AuthorBookSerializer, AddressSerializer, PublisherNrBooksSerializer
from .serializers import OneBookSerializer, OnePublisherSerializer, AuthorsSortedByNrBooksSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.db.models import Count, Sum


# Create your views here.
#for filtering ?'name of field'__'property'=criteria

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'nrOfPages':['gt', 'lt']}


class BookDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = OneBookSerializer


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PublisherList(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = OnePublisherSerializer


class AuthorBookList(generics.ListCreateAPIView):
    queryset = AuthorBook.objects.all()
    serializer_class = AuthorBookSerializer


class AuthorBookDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorBook.objects.all()
    serializer_class = AuthorBookSerializer


#display all the publishers based on the number of books published, field for number of books
class PublisherCountView(generics.ListAPIView):
    queryset = Publisher.objects.annotate(nrBooksPublished=Count('book')).order_by('-nrBooksPublished')
    serializer_class = PublisherNrBooksSerializer


#sort the authors based on the number of books they've written
class AuthorsSortedByNrBooksView(generics.ListAPIView):
    queryset = Author.objects.annotate(nrBooksWritten=Count('authorbook')).order_by('-nrBooksWritten')
    serializer_class = AuthorsSortedByNrBooksSerializer


class BooksToPublisherView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = OnePublisherSerializer

    def get_queryset(self, request, *args, **kwargs):
        return Publisher.objects.filter(pk=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        publisher = self.get_object()
        serializer = BookSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(publisherID=publisher)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

