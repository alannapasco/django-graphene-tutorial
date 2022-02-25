import graphene
#import inputs 

from .models import Books
from books.types import BooksType
from books.resolvers import resolve_all_books

#list of ALL queries related to books!
class BookQueries(graphene.ObjectType):
    all_books = graphene.List(BooksType)

    def resolve_all_books(root, info):
        #return Books.objects.all()
        #return Books.objects.filter(title="Django")
        return resolve_all_books(root, info)
