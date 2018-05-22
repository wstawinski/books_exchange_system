from django.contrib import admin

from book.models import Report
from search.models import Book

admin.site.register(Book)
admin.site.register(Report)
