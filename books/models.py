# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import uuid


class Category(models.Model):
    class Meta:
        verbose_name_plural="categories"

    name=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class ISBN(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author_title=models.CharField(max_length=255)
    book_title=models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField(max_length=2048, null=True, blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True,related_name="book")
    categories=models.ManyToManyField(Category,null=True,blank=True)
    isbn=models.OneToOneField(ISBN,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title