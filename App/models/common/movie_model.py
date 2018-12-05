

"""
insert into movies(id, showname, shownameen, director, leadingRole, type, country, language, duration,
screeningmodel, openday, backgroundpicture, flag, isdelete) values(228830,"梭哈人生","The Drifting Red Balloon",
"郑来志","谭佑铭,施予斐,赵韩樱子,孟智超,李林轩","剧情,爱情,喜剧","中国大陆","汉语普通话",90,"4D",date("2018-01-30 00:00:00"),
"i1/TB19_XCoLDH8KJjy1XcXXcpdXXa_.jpg",1,0);

"""
from App.ext import db
from App.models import BaseModel


class Movie(BaseModel):
    __tablename__ = "movies"
    showname = db.Column(db.String(64))
    shownameen = db.Column(db.String(128))
    director = db.Column(db.String(64))
    leadingRole = db.Column(db.String(256))
    type = db.Column(db.String(64))
    country = db.Column(db.String(64))
    language = db.Column(db.String(64))
    duration = db.Column(db.Integer, default=90)
    screeningmodel = db.Column(db.String(32))
    openday = db.Column(db.DateTime)
    backgroundpicture = db.Column(db.String(256))
    flag = db.Column(db.Boolean, default=False)
    is_delete = db.Column(db.Boolean, default=False)