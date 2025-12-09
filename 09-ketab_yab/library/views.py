from django.http import HttpResponse
from .models import Book
from .render import render_to_readable_output


def book_list(request):
    min_price = int(request.GET.get('min_price', 0) or 0)
    max_price = int(request.GET.get('max_price', 0) or 0)
    author = request.GET.get('author', '')
    name = request.GET.get('name', '')

    query = Book.objects.filter(name__icontains=name, author__icontains=author)
    if min_price >= 0:
        query = query.filter(price__gte = min_price)
    if max_price > min_price:
        query = query.filter(price__lte = max_price)

    rendered_string = render_to_readable_output(query)
    return HttpResponse(rendered_string)
