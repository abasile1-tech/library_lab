class Library:
	def __init__(self, books):
		self.books = books

	def list_all_books(self):
		return self.books

	def show_individual_book(self, title):
		for book in self.books:
			if book.title == title:
				return book

	def add_new_book_to_library(self):
		pass

	def remove_book_from_library(self):
		pass