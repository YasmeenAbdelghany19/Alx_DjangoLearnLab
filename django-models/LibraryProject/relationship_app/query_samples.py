from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author():
    """Query all books by a specific author."""
    try:
        # Get author by name
        author = Author.objects.get(name="John Doe")
        # Get all books by this author
        books = Book.objects.filter(author=author)
        print(f"Books by {author.name}:")
        for book in books:
            print(f"  - {book.title}")
    except Author.DoesNotExist:
        print("Author not found")

def list_books_in_library(library_name):
    """List all books in a library."""
    try:
        # Get library by name
        library = Library.objects.get(name=library_name)
        # Get all books in this library
        books = library.books.all()
        print(f"Books in {library.name}:")
        for book in books:
            print(f"  - {book.title}")
    except Library.DoesNotExist:
        print("Library not found")

def retrieve_librarian_for_library(library_name):
    """Retrieve the librarian for a library."""
    try:
        # Get library by name
        library = Library.objects.get(name=library_name)
        # Get librarian for this library
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library.name}: {librarian.name}")
    except Library.DoesNotExist:
        print("Library not found")
    except Librarian.DoesNotExist:
        print("Librarian not found for this library")

# Run the queries
if __name__ == "__main__":
    print("=== Relationship Queries Demo ===")
    query_books_by_author()
    print()
    list_books_in_library("Central Library")
    print()
    retrieve_librarian_for_library("Central Library")
