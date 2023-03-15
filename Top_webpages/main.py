from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from sqlalchemy import asc,desc


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

API_KEY = '5177b56dc20815f8d29b3aa5ca01f136'
API_URL = 'https://api.themoviedb.org/3/search/movie'

MOVIE_DB_IMAGE_URL = 'https://image.tmdb.org/t/p/w500'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


class MyNewMovie(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField('ADD')


class MyEdit(FlaskForm):
    rating = StringField("Your Rating", validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField('Done')


@app.route("/")
def home():
    data = movie.query.order_by(movie.rating).all()
    for i in range(len(data)):
        #This line gives each movie a new ranking reversed from their order in all_movies
        data[i].ranking = len(data) - i
        db.session.commit()
    return render_template("index.html", data=data)


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    form = MyEdit()
    if form.validate_on_submit():
        movie_id = request.args.get('id')
        update = movie.query.get(movie_id)
        update.rating = request.form['rating']
        update.review = request.form['review']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form)


@app.route('/all')
def show():
    data = movie.query.all()
    return render_template('all.html', data=data)


@app.route('/delete', methods=['POST', 'GET'])
def delete():
    movie_id = request.args.get('id')
    dt = movie.query.get(movie_id)
    db.session.delete(dt)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['POST', 'GET'])
def add():
    form = MyNewMovie()
    if form.validate_on_submit():
        name = request.form['title']
        return redirect(url_for('select', name=name))

    return render_template('add.html', form=form)


@app.route('/select')
def select():
    name = request.args.get('name')
    log = {
        'api_key': API_KEY,
        'query': name
    }

    response = requests.get(url=API_URL, params=log)
    response.raise_for_status()
    data = response.json()
    result = data['results']

    return render_template('select.html', result=result)


@app.route('/update')
def update():
    name = request.args.get('name')
    id = request.args.get('id')
    log = {
        'api_key': API_KEY,
        'query': name
    }

    response = requests.get(url=API_URL, params=log)
    response.raise_for_status()
    data = response.json()
    result = data['results']
    for dt in result:
        if dt['id'] == int(id):
            new_movie = movie(
                    title= dt['original_title'],
                    year= dt['release_date'].split("-")[0],
                    description= dt['overview'],
                    rating=7.3,
                    ranking=10,
                    review="My favourite character was the caller.",
                    img_url= f"{MOVIE_DB_IMAGE_URL}{dt['poster_path']}",
                )
            db.session.add(new_movie)
            db.session.commit()

    new_id = movie.query.filter_by(title= name).first()

    return redirect(url_for('edit', id=new_id.id))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
