from django.contrib import admin
from .models import Book

@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    fields = ('title','subtitle','author','isbn',)
    list_display = ('title','subtitle','author','isbn',)