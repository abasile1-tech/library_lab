import unittest
from models.book import Book
from models.library import Library

class TestBook(unittest.TestCase):
	def setUp(self):
		self.philoshophers_stone = Book("Harry Potter and the Philosoper's Stone", "J.K. Rowling", "Fantasy")
		self.programming_textbook = Book("Programming: Principles and Practice Using C++", "Bjarne Stroustrup", "Educational")
		self.hobbit = Book("The Hobbit", "J.R.R. Tolkien", "Fantasy")
		self.my_library = Library([self.philoshophers_stone, self.programming_textbook, self.hobbit])

	def test_list_all_books(self):
		self.assertEqual([self.philoshophers_stone, self.programming_textbook, self.hobbit], self.my_library.list_all_books())

	def test_show_individual_book(self):
		pass

	def test_add_new_book_to_library(self):
		pass

	def test_remove_book_from_library(self):
		pass