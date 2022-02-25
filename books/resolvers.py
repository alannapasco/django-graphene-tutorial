from .models import Books

def resolve_all_books(root, info):
    return Books.objects.all()