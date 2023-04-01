from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from db import db, Movie

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-collection.sqlite3'
db.init_app(app)

Bootstrap(app)

@app.route("/")
def home():
    with app.app_context():
                db.create_all()   

    first_movie = Movie(img_url="./static/images/drive.png", ranking=10, movie_name="Drive", rating="7.2", year="2011", review="Loved it!", summary="""A mysterious Hollywood
      stuntman and mechanic moonlights as a getaway driver and finds himself in trouble when he helps out his neighbor in this action drama""")
    
    db.session.add(first_movie)
    db.session.commit()

    return render_template("index.html", first_movie = first_movie)


if __name__ == '__main__':
    app.run(debug=True)
