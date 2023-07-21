from flask import render_template, request, redirect, Blueprint
from models.library import my_library

library_blueprint = Blueprint('library', __name__)

@library_blueprint.route('/')
def index():
	return render_template('index.html', title='Home')

@library_blueprint.route('/library')
def library():
	return render_template('library.html', title='Library', my_library=my_library)