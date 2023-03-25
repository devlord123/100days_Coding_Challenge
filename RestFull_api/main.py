from flask import Flask, jsonify, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


@app.route("/")
def home():
    data = Cafe.query.all()
    return render_template("index.html", data=data)

@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(random_cafe.to_dict())

@app.route('/all')
def get_all_cafe():
    cafe_list = db.session.query(Cafe).all()
    return jsonify(cafe_list = [cafe.to_dict() for cafe in cafe_list])


@app.route('/check', methods=['GET', 'POST'])
def search():
    query_location = request.args.get("loc")

    check = db.session.query(Cafe).filter_by(location=query_location).first()

    if check:
        return jsonify(check = check.to_dict())
    else:
        return {
            'error': {
                "Location": "Not Found"
            }
        }
    

    return render_template('search.html', loc=query_location)



@app.route("/add", methods=["POST", 'GET'])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

    

## HTTP GET - Read Record  PMAK-641a391f620eb3148ae009f7-abe34e738224ca58561ba3bfe67fe58dfe

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record

# postman login --with-api-key PMAK-641a391f620eb3148ae009f7-abe34e738224ca58561ba3bfe67fe58dfe
# postman api lint 79bec01b-e78f-4615-92a7-813bec806b4b

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
