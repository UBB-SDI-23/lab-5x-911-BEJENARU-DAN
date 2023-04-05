from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator

class Address(models.Model):
    country = models.CharField(max_length=200, null=True)
    county = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    street = models.CharField(max_length=200, null=True)
    streetNumber = models.IntegerField(null=True)

    def __str__(self):
        return f"Country: {self.country}, County: {self.county}, City: {self.city} + Street: {self.street} + Number: {self.streetNumber}"


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=200, null=True)
    foundingYear = models.DateField(null=True)
    email = models.CharField(max_length=200, null=True, validators=[EmailValidator()])
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    webAddress = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"Name: {self.name}, Founding year: {self.foundingYear}, Email: {self.email}, Address: {self.address}, web Address: {self.webAddress}"


class Book(models.Model):
    name = models.CharField(max_length=200, null=True)
    nrOfPages = models.IntegerField(null=True, validators=[MaxValueValidator(10000), MinValueValidator(0)])
    publisherID = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)
    releaseYear = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(2030)])
    genre = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"Name: {self.name}, Number of pages: {self.nrOfPages}, Publisher: {self.publisherID}, Release year: {self.releaseYear}, Genre: {self.genre}"


class Author(models.Model):
    firstName = models.CharField(max_length=200, null=True)
    lastName = models.CharField(max_length=200, null=True)
    dob = models.DateField("Date of Birth(mm/dd/yyyy)", null=True)
    nationality = models.CharField(max_length=200, null=True)
    areaOfInterest = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"First Name: {self.firstName}, Last Name: {self.lastName}, DOB: {self.dob}, Nationality: {self.nationality}, Area of Interest: {self.areaOfInterest}"


class AuthorBook(models.Model):
    bookID = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    authorID = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=200, null=True, choices=[('primary', 'Primary Author'), ('secondary', 'Co-Author')])
    contributionTime = models.IntegerField("(weeks)", null=True)

    def __str__(self):
        return f"Book ID: {self.bookID}, Author ID: {self.authorID}, Contribution Role: {self.role}, Contribution Time: {self.contributionTime}"


