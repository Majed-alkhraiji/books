from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

migrate = Migrate(app, db)


class Book(db.Model):
    def __init__(self, title, author, type, read):
        self.title = db.Column(db.String(), nullable=False)
        self.author = db.Column(db.String(), nullable=False)
        self.type = db.Column(db.String(), nullable=False)
        self.read = db.Column(db.Boolean, nullable=False)

# TODO: implment a GET request to fetch all books
@app.route('/')
def index():
    return render_template('my-books.html', books=Book.query.all()) 

# TODO: implment a POST request of adding a book
@app.route('/add-book', method=['POST'])
def addBook():
    book = []
    book['title'] = request.get_json()['title']
    book['author'] = request.get_json()['author']
    book['type'] = request.get_json()['type']
    book['read'] = False


    return redirect(url_for('my-books'))

# TODO: implment a PUT request to mark the book as read
@app.route('/update-status', method=['PUT'])
def update_status():
    status = request.get_json()['title']
    Book.query.filter_by(title=status).update({"read": True})

# TODO: implment a Delete request to delete a book
@app.route('delete-book', method=['PUT'])
def delete_book():
    status = request.get_json()['title']
    book = Book.query.filter_by(title=status)
    db.session.delete(book)

# Default port:
if __name__ == '__main__':
    app.run(debug=True)
