import unittest

import sys
sys.path.append('')

from app.shop import Library, Book, Client

class TestBook(unittest.TestCase):

    def test_check_out(self):
        book = Book("To Kill a Mockingbird", "Harper Lee")
        self.assertFalse(book.is_checked_out)
        book.check_out()
        self.assertTrue(book.is_checked_out)
        
    def test_check_in(self):
        book = Book("Pride and Prejudice", "Jane Austen")
        book.check_out()
        self.assertTrue(book.is_checked_out)
        book.check_in()
        self.assertFalse(book.is_checked_out)


class TestLibrary(unittest.TestCase):

    def test_add_book(self):
        library = Library()
        book = Book("To Kill a Mockingbird", "Harper Lee")
        self.assertEqual(len(library.books), 0)
        library.add_book(book)
        self.assertEqual(len(library.books), 1)
        self.assertEqual(library.books[0].title, "To Kill a Mockingbird")
        self.assertEqual(library.books[0].author, "Harper Lee")
        
    def test_check_out_book(self):
        library = Library()
        book = Book("To Kill a Mockingbird", "Harper Lee")
        library.add_book(book)
        library.check_out_book("To Kill a Mockingbird")
        self.assertTrue(book.is_checked_out)
        library.check_out_book("Pride and Prejudice")
        self.assertEqual(len(library.books), 1)
        
    def test_check_in_book(self):
        library = Library()
        book = Book("Pride and Prejudice", "Jane Austen")
        library.add_book(book)
        book.check_out()
        library.check_in_book("Pride and Prejudice")
        self.assertFalse(book.is_checked_out)
        library.check_in_book("Pride and Prejudice")
        self.assertEqual(len(library.books), 1)


class TestClient(unittest.TestCase):

    def test_check_out_book(self):
        library = Library()
        book1 = Book("To Kill a Mockingbird", "Harper Lee") 
        library.add_book(book1)
        book2 = Book("Pride and Prejudice", "Jane Austen") 
        library.add_book(book2)

        client = Client("John Doe") 
        client.check_out_book(library, "To Kill a Mockingbird")
        self.assertTrue(book1.is_checked_out)
        self.assertIn(book1, client.checked_out_books)

        client.check_out_book(library, "Pride and Prejudice")
        self.assertFalse(book2.is_checked_out)
        self.assertNotIn(book2, client.checked_out_books)


    def test_check_in_book(self):
        library = Library()
        book1 = Book("To Kill a Mockingbird", "Harper Lee") 
        library.add_book(book1)
        book2 = Book("Pride and Prejudice", "Jane Austen") 
        library.add_book(book2)
        
        client = Client("John Doe") 
        client.check_out_book(library, "To Kill a Mockingbird")
        self.assertTrue(book1.is_checked_out)
        self.assertIn(book1, client.checked_out_books)

        client.check_out_book(library, "Pride and Prejudice")
        self.assertTrue(book1.is_checked_out)
        self.assertIn(book1, client.checked_out_books)


if __name__ == '__main__':
    unittest.main()
