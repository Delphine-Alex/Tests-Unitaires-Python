import unittest

import sys
sys.path.append('')

from app.shop import Book

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

if __name__ == '__main__':
    unittest.main()


import unittest

import sys
sys.path.append('')

from app.shop import Library, Book

class TestLibrary(unittest.TestCase):

    def test_add_book(self):
        library = Library()
        book = Book("To Kill a Mockingbird", "Harper Lee")
        self.assertEqual(len(library.books), 0)
        library.add_book(book)
        self.assertEqual(len(library.books), 1)
        
    def test_check_out_book(self):
        library = Library()
        book = Book("To Kill a Mockingbird", "Harper Lee")
        library.add_book(book)
        library.check_out_book("To Kill a Mockingbird")
        self.assertTrue(book.is_checked_out)
        
    def test_check_in_book(self):
        library = Library()
        book = Book("Pride and Prejudice", "Jane Austen")
        library.add_book(book)
        book.check_out()
        library.check_in_book("Pride and Prejudice")
        self.assertFalse(book.is_checked_out)

if __name__ == '__main__':
    unittest.main()


import unittest

import sys
sys.path.append('')

from app.shop import Library, Book, Client

class TestClient(unittest.TestCase):

    def test_check_out_book(self):
        library = Library()
        book = Book("To Kill a Mockingbird", "Harper Lee")
        library.add_book(book)
        client = Client("John Doe")
        self.assertEqual(len(client.checked_out_books), 0)
        client.check_out_book(library, "To Kill a Mockingbird")
        self.assertEqual(len(client.checked_out_books), 1)
        self.assertTrue(book.is_checked_out)
        
    def test_check_in_book(self):
        library = Library()
        book = Book("Pride and Prejudice", "Jane Austen")
        library.add


if __name__ == '__main__':
    unittest.main()
