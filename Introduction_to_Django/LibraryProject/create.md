>>> from bookshelf.models import Books
>>> book = Books.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> print(book.id, book.title, book.author, book.publication_year)

# Expected Output:
# 1 1984 George Orwell 1949
