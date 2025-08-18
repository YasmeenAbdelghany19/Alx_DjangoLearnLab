from django.contrib import admin
from .models import Book

# Customize the admin interface to display title, author, and publication_year in the admin list view
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

# Configure list filters and search capabilities to enhance the admin’s usability for Book entries.
admin.site.register(Book, BookAdmin)