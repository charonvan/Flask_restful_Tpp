from App.ext import db
from App.models import BaseModel
from App.models.cinema_admin.cinema_address_model import CinemaAddress


class Hall(BaseModel):

    h_address_id = db.Column(db.Integer, db.ForeignKey(CinemaAddress.id))
    h_num = db.Column(db.Integer, default=1)
    h_seats = db.Column(db.String(128))

