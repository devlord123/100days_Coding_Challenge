from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


all_books = []

with app.app_context():
    db.create_all()
    all_books = db.session.query(Book).all()


# print(all_books)


@app.route('/')
def home():
    empty = False
    if all_books == []:
        empty = True
    books = all_books
    return render_template('index.html', books=books, empty=empty)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == "POST":
        # CREATE RECORD
        new_book = Book(
            title=request.form["book"],
            author=request.form["auth"],
            rating=request.form["rat"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html')


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    if request.method == "POST":
        #UPDATE RECORD
        book_id = request.form.get('id')
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit.html", book=book_selected)


@app.route('/delete')
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)


