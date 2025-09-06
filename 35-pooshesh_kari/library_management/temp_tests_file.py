from django.test import TestCase
from .models import Book, Author
import datetime

class ViewTests(TestCase):
    def setUp(self):
        today = datetime.date.today()
        self.author1 = Author.objects.create(first_name='author1', last_name='author1', date_of_birth=datetime.date(today.year - 40, today.month, today.day))
        self.author2 = Author.objects.create(first_name='author2', last_name='author2', date_of_birth=datetime.date(today.year - 80, today.month, today.day), date_of_death=datetime.date(today.year - 10, today.month, today.day))
        self.book1 = Book.objects.create(title='title1', author=self.author1, summary='summary', date_of_publish=datetime.date(today.year - 2, today.month, today.day))
        self.book2 = Book.objects.create(title='title2', author=self.author1, summary='summary', date_of_publish=datetime.date(today.year - 5, today.month, today.day))
        self.book3 = Book.objects.create(title='title3', author=self.author2, summary='summary', date_of_publish=datetime.date(today.year - 15, today.month, today.day))

    def test_booklist_view(self):
        response = self.client.get('/booklist/50/10/')
        self.assertTrue(b'<title>Booklist</title>' in response.content)
        self.assertEqual(response.context['good_books'], [self.book1, self.book2])
        self.assertEqual(response.context['bad_books'], [self.book3])

class ModelsTests(TestCase):
    def setUp(self):
        today = datetime.date.today()
        self.author1 = Author.objects.create(first_name='author1', last_name='author1', date_of_birth=datetime.date(today.year - 40, today.month, today.day))
        self.author2 = Author.objects.create(first_name='author2', last_name='author2', date_of_birth=datetime.date(today.year - 80, today.month, today.day), date_of_death=datetime.date(today.year - 10, today.month, today.day))
        self.book1 = Book.objects.create(title='title1', author=self.author1, summary='summary', date_of_publish=datetime.date(today.year - 2, today.month, today.day))
        self.book2 = Book.objects.create(title='title2', author=self.author1, summary='summary', date_of_publish=datetime.date(today.year - 5, today.month, today.day))
        self.book3 = Book.objects.create(title='title3', author=self.author2, summary='summary', date_of_publish=datetime.date(today.year - 15, today.month, today.day))

    def test_author_name(self):
        self.assertEqual(self.author1.__str__(), 'author1 author1')

    def test_author_is_alive(self):
        self.assertTrue(self.author1.is_alive())
        self.assertFalse(self.author2.is_alive())

    def test_author_age(self):
        self.assertEqual(self.author1.get_age(), datetime.date.today() - self.author1.date_of_birth)
        self.assertEqual(self.author2.get_age(), self.author2.date_of_death - self.author2.date_of_birth)

    def test_book_name(self):
        self.assertEqual(self.book1.__str__(), 'title1')

    def test_book_age(self):
        self.assertEqual(self.book1.get_age(), datetime.date.today() - self.book1.date_of_publish)
