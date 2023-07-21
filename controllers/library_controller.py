from flask import render_template, request, redirect, Blueprint
from models.library import my_library

library_blueprint = Blueprint('library', __name__)

@library_blueprint.route('/')
def index():
	return render_template('index.html', title='Index')

@library_blueprint.route('/library')
def library():
	return render_template('library.html', title='Library', my_library=my_library)

@library_blueprint.route('/library/<book_title>')
def book(book_title):
	book = my_library.show_individual_book(book_title)
	return render_template('book.html', title=book_title, book=book)