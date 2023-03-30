"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ProjectSDI import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Book/', views.BookList.as_view()), # path for the book list
    path('Book/<int:pk>/', views.BookDetails.as_view()), # path for the details of a certain book
    path('Address/', views.AddressList.as_view()),
    path('Address/<int:pk>/', views.AddressDetails.as_view()),
    path('Publisher/', views.PublisherList.as_view()),
    path('Publisher/<int:pk>/', views.PublisherDetails.as_view()),
    path('Publisher/<int:pk>/Books/', views.BooksToPublisherView.as_view()),
    path('Author/', views.AuthorList.as_view()),
    path('Author/<int:pk>/', views.AuthorDetails.as_view()),
    path('AuthorBook/', views.AuthorBookList.as_view()),
    path('AuthorBook/<int:pk>/', views.AuthorBookDetails.as_view()),
    path('Publisher/PublisherCountbyBooks/', views.PublisherCountView.as_view()),
    path('Author/AuthorSortedByNrBooks/', views.AuthorsSortedByNrBooksView.as_view())
]


