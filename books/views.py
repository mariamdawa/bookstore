# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book


def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html',{
        "books": books
    })


def create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'books/create.html', {
        'form': form
    })


def edit(request, id):
    book = Book.objects.get(pk=id)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'books/edit.html', {
        'form': form,
        'book': book
    })


def delete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('index')

