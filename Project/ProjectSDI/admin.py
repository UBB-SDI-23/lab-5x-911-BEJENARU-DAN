from django.contrib import admin
from .models import Book, AuthorBook, Author, Publisher
# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(AuthorBook)
