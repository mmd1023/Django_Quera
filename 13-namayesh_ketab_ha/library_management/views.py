from .models import Book
from django.shortcuts import render


def booklist(request):
    return render(request, 'booklist.html', {
        'books': Book.objects.all()
    })
