from rest_framework import serializers
from .models import Book, Author, Publisher, AuthorBook, Address
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'nrOfPages', 'publisherID', 'releaseYear', 'genre']

    def create(self, validated_data):
        if isinstance(validated_data, list):
            books = [Book(**item) for item in validated_data]
            Book.objects.bulk_create(books)
            return books
        else:
            book = Book.objects.create(**validated_data)
            return book


class OneBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('__all__')
        depth = 9


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'firstName', 'lastName', 'dob', 'nationality', 'areaOfInterest']



class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'foundingYear', 'email', 'address', 'webAddress']


class OnePublisherSerializer(serializers.ModelSerializer):
    books = BookSerializer(source='book_set', many=True)
    class Meta:
        model = Publisher
        fields = ('__all__')
        expandable_fields = {"book_set": (BookSerializer, {"source": "book_set"})}


class AuthorBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorBook
        fields = ['id', 'bookID', 'authorID', 'role', 'contributionTime']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'country', 'county', 'city', 'street', 'streetNumber']


class PublisherNrBooksSerializer(serializers.ModelSerializer):
    nrBooksPublished = serializers.IntegerField()
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'nrBooksPublished']


class AuthorsSortedByNrBooksSerializer(serializers.ModelSerializer):
    nrBooksWritten = serializers.IntegerField()
    class Meta:
        model = Author
        fields = ['id', 'firstName', 'lastName', 'nrBooksWritten']
