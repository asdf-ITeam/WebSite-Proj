from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

#flask --app main --debug run
#source env/bin/activate

db = SQLAlchemy()
admin = Admin()
DB_NAME = "database.db"

class PostView(ModelView):
    can_delete=False
    form_columns=["amount","date","user"]
    column_list = ["amount", "date", "user_name"]




def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "hello"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    from .models import User, Credit, Article  # Import inside the function to avoid circular import
    admin.add_view(ModelView(User,db.session))
    admin.add_view(ModelView(Article,db.session))
    admin.add_view(PostView(Credit,db.session))

    db.init_app(app)
    admin.init_app(app)
    



    from .views import views
    from .auth import auth
    

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'views.home'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        # Import inside the function to avoid circular import
        from .models import User
        return User.query.get(int(id))

    return app
