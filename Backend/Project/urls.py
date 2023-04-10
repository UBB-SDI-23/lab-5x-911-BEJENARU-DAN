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
from django.urls import path, include

from ProjectSDI.views.AddressView import AddressList, AddressDetails
from ProjectSDI.views.AuthorBookView import AuthorBookList, AuthorBookDetails
from ProjectSDI.views.AuthorsSortedByNrBooksView import AuthorsSortedByNrBooksView
from ProjectSDI.views.AuthorView import AuthorList, AuthorDetails
from ProjectSDI.views.BookView import BookList, BookDetails, BooksToPublisherView
from ProjectSDI.views.PublisherCountView import PublisherCountView
from ProjectSDI.views.PublisherView import PublisherList, PublisherDetails

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/Book/', BookList.as_view()), # path for the book list
    path('api/Book/<int:pk>/', BookDetails.as_view()), # path for the details of a certain book
    path('api/Address/', AddressList.as_view()),
    path('api/Address/<int:pk>/', AddressDetails.as_view()),
    path('api/Publisher/', PublisherList.as_view()),
    path('api/Publisher/<int:pk>/', PublisherDetails.as_view()),
    path('api/Publisher/<int:pk>/Books/', BooksToPublisherView.as_view()),
    path('api/Author/', AuthorList.as_view()),
    path('api/Author/<int:pk>/', AuthorDetails.as_view()),
    path('api/AuthorBook/', AuthorBookList.as_view()),
    path('api/AuthorBook/<int:pk>/', AuthorBookDetails.as_view()),
    path('api/Publisher/PublisherCountbyBooks/', PublisherCountView.as_view()),
    path('api/Author/AuthorSortedByNrBooks/', AuthorsSortedByNrBooksView.as_view()),
    path('api/swagger/schema/', SpectacularAPIView.as_view(), name = 'schema'),
    path('api/swagger/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]


