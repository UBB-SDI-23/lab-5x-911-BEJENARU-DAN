from rest_framework.views import APIView
from rest_framework import generics

from ..models import Book, Publisher
from ..serializers import BookSerializer, PublisherSerializer
from ..serializers import OneBookSerializer, OnePublisherSerializer

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'nrOfPages':['gt', 'lt']}


class BookDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = OneBookSerializer


# Add books to an existing publisher
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