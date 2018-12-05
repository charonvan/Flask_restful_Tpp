from App.ext import db
from App.models import BaseModel
from App.models.cinema_admin.cinema_hall_model import Hall
from App.models.common.movie_model import Movie


class HallMovie(BaseModel):

    h_movie_id = db.Column(db.Integer, db.ForeignKey(Movie.id))

    h_hall_id = db.Column(db.Integer, db.ForeignKey(Hall.id))

    h_time = db.Column(db.DateTime)

