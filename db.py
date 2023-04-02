from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    """ front class members"""
    id = db.Column(db.Integer, primary_key=True)
    img_url = db.Column(db.String, unique=True, nullable=False)
    ranking = db.Column(db.Integer, unique=False, nullable=False)

    """ back class members"""
    movie_name = db.Column(db.String, unique=True, nullable=False)
    rating = db.Column(db.String, nullable=False)
    year = db.Column(db.String, unique=False, nullable=False)
    review = db.Column(db.String, unique=False, nullable=False)
    summary = db.Column(db.String, unique=True, nullable=False)


    def __init__(self, img_url:str, ranking:int, movie_name:str, rating:str, year:str, review:str, summary:str) -> None:
           self.img_url = img_url
           self.ranking = ranking
           self.movie_name = movie_name
           self.rating = rating
           self.year = year
           self.review = review
           self.summary = summary

