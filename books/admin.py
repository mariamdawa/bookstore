# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Book,Category,ISBN
from .forms import BookForm,CategoryForm

# Register your models here.



class BookInline(admin.StackedInline):
    model=Book
    max_num=1
    extra=1

class CategoryAdmin(admin.ModelAdmin):
    form=CategoryForm
    list_display=("name",)
    search_fields=("name",)
    
class  BookAdmin(admin.ModelAdmin):
    form=BookForm
    list_display=("title","user","content")
    list_filter=("categories",)
    search_fields=("title",)
    
    
class ISBNAdmin(admin.ModelAdmin):
    list_display=("id","author_title")
    inlines=[BookInline]


admin.site.register(Book,BookAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(ISBN,ISBNAdmin)
