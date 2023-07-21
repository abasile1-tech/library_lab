from flask import render_template, request, redirect, Blueprint
from models.library import my_library
from models.book import Book

library_blueprint = Blueprint('library', __name__)

@library_blueprint.route('/')
def index():
	return render_template('index.html', title='Index')

@library_blueprint.route('/library')
def library():
	books = my_library.list_all_books()
	return render_template('library.html', title='Library', books=books)

@library_blueprint.route('/library/<book_title>')
def book(book_title):
	book = my_library.show_individual_book(book_title)
	return render_template('book.html', title=book_title, book=book)

@library_blueprint.route('/library/delete/<book_title>', methods=['POST'])
def delete_book(book_title):
	my_library.remove_book_from_library(book_title)
	return redirect('/library')

@library_blueprint.route('/library/add', methods=['POST'])
def add_book():
	title = request.form['title']
	author = request.form['author']
	genre = request.form['genre']
	book = Book(title, author, genre)
	my_library.add_new_book_to_library(book)
	return redirect('/library')
