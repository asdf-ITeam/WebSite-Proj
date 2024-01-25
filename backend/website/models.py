from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#admin be implement
#method for credit
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    phone_number = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(150))

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name} : {self.id}"
    
    # Relationship with Credit
    credits = db.relationship("Credit", back_populates="user")


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    slug = db.Column(db.String(255), unique=True, nullable=False)
    date_published = db.Column(db.DateTime(timezone=True), default=func.now())

    

class Credit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    
    
    # Relationship with User
    user = db.relationship("User", back_populates="credits")
    @property
    def user_name(self):
        return f"{self.user.first_name} {self.user.last_name}" if self.user else ""
