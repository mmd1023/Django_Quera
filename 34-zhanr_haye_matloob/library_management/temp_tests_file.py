from django.test import TestCase
from .models import Book


class TestAPI(TestCase):
    def setUp(self):
        for i in range(10):
            Book.objects.create(title = f'title{i+1}', genre = 'genre1')
        for i in range(20):
            Book.objects.create(title = f'title{i+21}', genre = 'genre2')
        for i in range(30):
            Book.objects.create(title = f'title{i+31}', genre = 'genre3')

    def test_books_view(self):
        for i in range(3):
            book_count = Book.objects.count()
            response = self.client.get(f'/books/genre{i+1}/')
            self.assertEqual(book_count, Book.objects.count())

            self.assertNotEqual(response.status_code, 404)

            data = response.json()

            self.assertEqual(data.get('title'), 'List of Books')
            self.assertEqual(data.get('genre'), f'genre{i+1}')
            self.assertEqual(data.get('books'), list(Book.objects.filter(genre=f'genre{i+1}').values_list('id', flat=True)))