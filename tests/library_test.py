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
		self.assertEqual(self.hobbit, self.my_library.show_individual_book("The Hobbit"))

	def test_add_new_book_to_library(self):
		chamber_of_secrets = Book("Harry Potter and the Chamber of Secrets", "J.K. Rowling", "Fantasy")
		self.my_library.add_new_book_to_library(chamber_of_secrets)
		self.assertEqual([self.philoshophers_stone, self.programming_textbook, self.hobbit, chamber_of_secrets], self.my_library.list_all_books())

	def test_remove_book_from_library(self):
		chamber_of_secrets = Book("Harry Potter and the Chamber of Secrets", "J.K. Rowling", "Fantasy")
		self.my_library.add_new_book_to_library(chamber_of_secrets)
		self.my_library.remove_book_from_library("Harry Potter and the Philosoper's Stone")
		self.assertEqual([self.programming_textbook, self.hobbit, chamber_of_secrets], self.my_library.list_all_books())