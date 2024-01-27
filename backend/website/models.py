from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


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


class Admin(User):  # Inherit from User class
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    admin_property = db.Column(db.Boolean)  
    def __repr__(self) -> str:
        return f"Admin {self.first_name} {self.last_name} : {self.id}"

    def promoteUser(self, user):

        if isinstance(user, User):
            user.admin_property = "Admin granted"
            db.session.commit()

    def sendNotification(self, message):
        all_users = User.query.all()
        for user in all_users:
            print(f"Notification sent to {user.first_name} {user.last_name}: {message}")

    def editUser(self,name:str,lastname:str,user:User):
        user.last_name=lastname
        user.first_name=name
    
    def changePassword(self,password:str,user:User):
        user.password=password
        



class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    slug = db.Column(db.String(255), unique=True, nullable=False)
    date_published = db.Column(db.DateTime(timezone=True), default=func.now())

    def updateTitle(self,title:str):
        self.title = title

    def updateBody(self,body:str):
        self.body = body


class Gallery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)

    def __repr__(self) -> str:
        return f"Gallery: {self.title} ({self.id})"

    def addPhoto(self):
        pass #to be implemented

    def deletePhoto(self ):
        pass #to be implemented

    def updateCaption(self, description: str):
        self.caption = description

    

class Credit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())


    def changeCredit(self,val):
        self.amout+=val
        return val

    def checkOut(self):
        self.amout=0

    
    # Relationship with User
    user = db.relationship("User", back_populates="credits")
    @property
    def user_name(self):
        return f"{self.user.first_name} {self.user.last_name}" if self.user else ""
