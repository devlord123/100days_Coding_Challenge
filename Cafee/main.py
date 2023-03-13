from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe location (URL)", validators=[DataRequired(), URL()])
    opent = StringField("Opening Time", validators=[DataRequired()])
    closeT = StringField("Close Time", validators=[DataRequired()])
    cofeeR = StringField("Coffe Ranking", validators=[DataRequired()])
    wifi = StringField("Wifi Strength", validators=[DataRequired()])
    power = StringField("Power", validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", 'a') as file:
            file.write(
                f"\n{form.cafe.data},"
                f'{form.location.data},'
                f'{form.opent.data},'
                f'{form.closeT.data},'
                f'{form.cofeeR.data},'
                f'{form.wifi.data},'
                f'{form.power.data},'

            )
            return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
