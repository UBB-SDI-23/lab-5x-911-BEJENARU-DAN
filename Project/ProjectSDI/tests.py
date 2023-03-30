from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase

from .models import Book, Publisher, Author, AuthorBook, Address
class PublisherCountViewTestcase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        #create address, publisher, book
        #Address
        address1 = Address.objects.create(country="ROMANIA", county="CLUJ", city="CLUJ-NAPOCA", street="MIHAIL KOGALNIGEANU", streetNumber=60)
        address2 = Address.objects.create(country="ROMANIA", county="NEAMT", city="ROMAN", street="ROMAN MUSAT", streetNumber=31)
        address3 = Address.objects.create(country="ROMANIA", county="BUCURESTI", city="BUCURESTI", street="MIHAI EMINESCU", streetNumber=14)
        address4 = Address.objects.create(country="ROMANIA", county="IASI", city="IASI", street="ALEXANDRU MACEDON", streetNumber=21)

        #Publisher
        publisher1 = Publisher.objects.create(name="HUMANITAS", foundingYear="2000-02-01", email="humanitas@email.ro", address=address4, webAddress="www.humanitas.ro")
        publisher2 = Publisher.objects.create(name="LITERA", foundingYear="1989-04-02", email="litera@email.com", address=address1, webAddress="www.litera.ro")
        publisher3 = Publisher.objects.create(name="MINERVA", foundingYear="1970-03-05", email="minerva@email.com", address=address3, webAddress="www.minerva.ro")
        publisher4 = Publisher.objects.create(name="NEMIRA", foundingYear="1991-05-03", email="nemira@email.com", address=address2, webAddress="www.nemira.ro")

        #Book
        book1 = Book.objects.create(name="Book1", nrOfPages=300, publisherID=publisher2, releaseYear=2000, genre="GENRE1")
        book2 = Book.objects.create(name="Book2", nrOfPages=400, publisherID=publisher2, releaseYear=2000, genre="GENRE1")
        book3 = Book.objects.create(name="Book3", nrOfPages=500, publisherID=publisher2, releaseYear=2000, genre="GENRE1")
        book4 = Book.objects.create(name="Book4", nrOfPages=250, publisherID=publisher4, releaseYear=2002, genre="GENRE2")
        book5 = Book.objects.create(name="Book5", nrOfPages=300, publisherID=publisher1, releaseYear=2003, genre="GENRE1")
        book6 = Book.objects.create(name="Book6", nrOfPages=310, publisherID=publisher1, releaseYear=2003, genre="GENRE1")


    def test_url_exists(self):
        response = self.client.get("/Publisher/PublisherCountbyBooks/")
        self.assertEqual(response.status_code, 200)


    def test_publisher_by_nr_books(self):
        response = self.client.get("/Publisher/PublisherCountbyBooks/")
        self.assertEqual(len(response.data), 4)
        first = response.data[0]
        second = response.data[1]
        third = response.data[2]
        fourth = response.data[3]
        self.assertEqual(first['name'], "LITERA")
        self.assertEqual(second['name'], "HUMANITAS")
        self.assertEqual(third['name'], "NEMIRA")
        self.assertEqual(fourth['name'], "MINERVA")


class AuthorsSortedByNrBooksViewTestcase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        #create address, publisher, book
        #Address
        address1 = Address.objects.create(country="ROMANIA", county="CLUJ", city="CLUJ-NAPOCA", street="MIHAIL KOGALNIGEANU", streetNumber=60)
        address2 = Address.objects.create(country="ROMANIA", county="NEAMT", city="ROMAN", street="ROMAN MUSAT", streetNumber=31)
        address3 = Address.objects.create(country="ROMANIA", county="BUCURESTI", city="BUCURESTI", street="MIHAI EMINESCU", streetNumber=14)
        address4 = Address.objects.create(country="ROMANIA", county="IASI", city="IASI", street="ALEXANDRU MACEDON", streetNumber=21)

        #Publisher
        publisher1 = Publisher.objects.create(name="HUMANITAS", foundingYear="2000-02-01", email="humanitas@email.ro", address=address4, webAddress="www.humanitas.ro")
        publisher2 = Publisher.objects.create(name="LITERA", foundingYear="1989-04-02", email="litera@email.com", address=address1, webAddress="www.litera.ro")
        publisher3 = Publisher.objects.create(name="MINERVA", foundingYear="1970-03-05", email="minerva@email.com", address=address3, webAddress="www.minerva.ro")
        publisher4 = Publisher.objects.create(name="NEMIRA", foundingYear="1991-05-03", email="nemira@email.com", address=address2, webAddress="www.nemira.ro")

        #Book
        book1 = Book.objects.create(name="Book1", nrOfPages=300, publisherID=publisher2, releaseYear=2000, genre="GENRE1")
        book2 = Book.objects.create(name="Book2", nrOfPages=400, publisherID=publisher2, releaseYear=2000, genre="GENRE1")
        book3 = Book.objects.create(name="Book3", nrOfPages=500, publisherID=publisher2, releaseYear=2000, genre="GENRE1")
        book4 = Book.objects.create(name="Book4", nrOfPages=250, publisherID=publisher4, releaseYear=2002, genre="GENRE2")
        book5 = Book.objects.create(name="Book5", nrOfPages=300, publisherID=publisher1, releaseYear=2003, genre="GENRE1")
        book6 = Book.objects.create(name="Book6", nrOfPages=310, publisherID=publisher1, releaseYear=2003, genre="GENRE1")

        #Authors
        author1 = Author.objects.create(firstName="FIRSTNAME1", lastName="LASTNAME1", dob="2023-03-26",
                                        nationality="NATIONALITY1", areaOfInterest="AREA1")
        author2 = Author.objects.create(firstName="FIRSTNAME2", lastName="LASTNAME2", dob="2023-03-26",
                                        nationality="NATIONALITY2", areaOfInterest="AREA2")
        author3 = Author.objects.create(firstName="FIRSTNAME3", lastName="LASTNAME3", dob="2023-03-26",
                                        nationality="NATIONALITY3", areaOfInterest="AREA3")
        author4 = Author.objects.create(firstName="FIRSTNAME4", lastName="LASTNAME4", dob="2023-03-26",
                                        nationality="NATIONALITY4", areaOfInterest="AREA4")
        author5 = Author.objects.create(firstName="FIRSTNAME5", lastName="LASTNAME5", dob="2023-03-26",
                                        nationality="NATIONALITY5", areaOfInterest="AREA5")
        author6 = Author.objects.create(firstName="FIRSTNAME6", lastName="LASTNAME6", dob="2023-03-26",
                                        nationality="NATIONALITY6", areaOfInterest="AREA6")

        #AuthorBook
        authorbook1 = AuthorBook.objects.create(bookID=book1, authorID=author1, role="primary", contributionTime=10)
        authorbook2 = AuthorBook.objects.create(bookID=book1, authorID=author2, role="secondary", contributionTime=10)
        authorbook3 = AuthorBook.objects.create(bookID=book2, authorID=author1, role="primary", contributionTime=10)
        authorbook4 = AuthorBook.objects.create(bookID=book3, authorID=author1, role="primary", contributionTime=10)
        authorbook5 = AuthorBook.objects.create(bookID=book4, authorID=author5, role="primary", contributionTime=10)
        authorbook6 = AuthorBook.objects.create(bookID=book5, authorID=author5, role="primary", contributionTime=10)
        authorbook7 = AuthorBook.objects.create(bookID=book6, authorID=author3, role="primary", contributionTime=10)
        authorbook8 = AuthorBook.objects.create(bookID=book2, authorID=author2, role="secondary", contributionTime=10)
        authorbook9 = AuthorBook.objects.create(bookID=book3, authorID=author1, role="secondary", contributionTime=10)


    def test_url_exists(self):
        response = self.client.get("/Author/AuthorSortedByNrBooks/")
        self.assertEqual(response.status_code, 200)


    def test_publisher_by_nr_books(self):
        response = self.client.get("/Author/AuthorSortedByNrBooks/")
        self.assertEqual(len(response.data), 6)
        first = response.data[0]
        second = response.data[1]
        third = response.data[2]
        fourth = response.data[3]
        fifth = response.data[4]
        sixth = response.data[5]
        self.assertEqual(first['firstName'], "FIRSTNAME1")
        self.assertEqual(second['firstName'], "FIRSTNAME2")
        self.assertEqual(third['firstName'], "FIRSTNAME5")
        self.assertEqual(fourth['firstName'], "FIRSTNAME3")
        self.assertEqual(fifth['firstName'], "FIRSTNAME4")
        self.assertEqual(sixth['firstName'], "FIRSTNAME6")

