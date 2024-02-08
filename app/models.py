from datetime import datetime
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()


class Cupcake(db.Model):

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String(50), nullable=False)
    size = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable=False, default='')
    image = db.Column(db.Text, nullable=False, default='')

    @classmethod
    def __repr__(self):
        return f"<User id:{self.id} {self.first_name} {self.last_name}>"