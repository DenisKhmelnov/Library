from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from retraining.library.models import Book, Reader, Author

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'author_link', 'quantity')
    list_display_links = ('title',)

    def author_link(self, obj):
        url = reverse("admin:library_author_change", args=[obj.author.id])
        return format_html('<a href="{}">{}</a>', url, obj.author)

    author_link.short_description = 'Author'

class ReaderAdmin(admin.ModelAdmin):
    list_display = ('id','name','surname','phone','status')
    list_filter = ('status',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'picture')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Reader, ReaderAdmin)
