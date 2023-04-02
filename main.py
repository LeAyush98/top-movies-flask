from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
import requests
from db import db, Movie
import os.path
from edit_form import MovieForm
from add_form import AddMovieForm
from movie_api import MovieAPI

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-collection.sqlite3'
db.init_app(app)

Bootstrap(app)

@app.route("/")
def home():
    with app.app_context():
        db.create_all()   

    if os.path.exists("./instance/movie-collection.sqlite3"):
        pass
    else:  
        first_movie = Movie(img_url="./static/images/drive.png", ranking=10, movie_name="Drive", rating="7.2", year="2011", review="Loved it!", summary="""A mysterious Hollywood
        stuntman and mechanic moonlights as a getaway driver and finds himself in trouble when he helps out his neighbor in this action drama""")
        db.session.add(first_movie)
        db.session.commit()
    
    return render_template("index.html", movies = db.session.query(Movie).all()) # important, do not forget

@app.route("/edit/<name>?id=<id>", methods= ["GET", "POST"])
def edit(name,id):
    form = MovieForm()
    if request.method == "GET":
        
        return render_template("edit.html", name=name, form = form, id=id)
    elif request.method == "POST":
        movie = Movie.query.filter_by(movie_name=name).first()   
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        
        return redirect(url_for("home"))   
    
@app.route("/delete/<name>", methods= ["POST", "GET"])
def delete(name):
    movie = Movie.query.filter_by(movie_name=name).first()   
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))   

@app.route("/add", methods= ["POST", "GET"])
def add():
    form = AddMovieForm()
    if request.method == "GET":
        return render_template("add.html", form=form)
    elif request.method == "POST":
        movie_name = form.name.data
        movie = MovieAPI(movie_name)
        return render_template("select.html", movies = movie.search(), api_key = movie.API_KEY, details_url = movie.MORE_INFO_URL)

if __name__ == '__main__':
    app.run(debug=True)
