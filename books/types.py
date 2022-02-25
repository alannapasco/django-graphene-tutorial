from graphene_django import DjangoObjectType
from .models import Books


class BooksType(DjangoObjectType):
    #helps serializing the data
    class Meta:
        model = Books
        fields = ("id", "title", "excerpt")
