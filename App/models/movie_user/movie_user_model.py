from werkzeug.security import generate_password_hash, check_password_hash

from App.ext import db
from App.models import BaseModel
from App.models.movie_user.model_constant import PERMISSION_NONE


COMMON_USER = 0
BLACK_USER = 1
VIP_USER = 2



class MovieUser(BaseModel):

    username = db.Column(db.String(32), unique=True)
    _password = db.Column(db.String(256))
    phone = db.Column(db.String(32), unique=True)
    is_delete = db.Column(db.Boolean, default=False)
    permission = db.Column(db.Integer, default=PERMISSION_NONE)

    @property
    def password(self):
        raise Exception("can't access")

    @password.setter
    def password(self, password_value):
        self._password = generate_password_hash(password_value)

    def check_password(self, password_value):
        return check_password_hash(self._password, password_value)

    def check_permission(self, permission):
        if (BLACK_USER & self.permission) == BLACK_USER:
            return False
        else:
            return permission & self.permission == permission
