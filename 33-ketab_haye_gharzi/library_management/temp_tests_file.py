from django.test import TestCase
from .models import Book, Borrowed, Member


class Tests(TestCase):
    def setUp(self):
        member1 = Member.objects.create(first_name='member1', last_name='memberi1')
        member2 = Member.objects.create(first_name='member2', last_name='memberi2')

        for i in range(13):
            Book.objects.create(title=f'book{i+1}', genre='genre1')
        for i in range(11):
            Book.objects.create(title=f'book{i+14}', genre='genre2')


        Borrowed.objects.create(member_id = 1, book_id = 1)
        Borrowed.objects.create(member_id = 1, book_id = 5)
        Borrowed.objects.create(member_id = 1, book_id = 20)

        Borrowed.objects.create(member_id = 2, book_id = 10)
        Borrowed.objects.create(member_id = 2, book_id = 15)
        Borrowed.objects.create(member_id = 2, book_id = 17)
        Borrowed.objects.create(member_id = 2, book_id = 22)

    def test_borrowed_books(self):        
        member1 = Member.objects.get(first_name='member1')
        member2 = Member.objects.get(first_name='member2')

        book_1_1 = Borrowed.objects.filter(member__id = member1.pk, book__genre = 'genre1').values_list('book__id', flat=True)
        book_1_2 = Borrowed.objects.filter(member__id = member1.pk, book__genre = 'genre2').values_list('book__id', flat=True)
        book_2_1 = Borrowed.objects.filter(member__id = member2.pk, book__genre = 'genre1').values_list('book__id', flat=True)
        book_2_2 = Borrowed.objects.filter(member__id = member2.pk, book__genre = 'genre2').values_list('book__id', flat=True)

        self.assertEqual(list(book_1_1), member1.borrowed_books('genre1'))
        self.assertEqual(list(book_1_2), member1.borrowed_books('genre2'))
        self.assertEqual(list(book_2_1), member2.borrowed_books('genre1'))
        self.assertEqual(list(book_2_2), member2.borrowed_books('genre2'))