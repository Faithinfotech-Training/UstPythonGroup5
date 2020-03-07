from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_pymongo import PyMongo
<<<<<<< HEAD

=======
>>>>>>> 1d4ca6ea4edc5a2590f45936cdda84786a7b007e
from app_package.config import Config

app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate=Migrate(app,db)
mongo=PyMongo(app)

<<<<<<< HEAD


from app_package import routes
=======
#login_manager=LoginManager(app)
#login_manager.login_view="index"

from app_package import resource_routes,batchroutes
>>>>>>> 1d4ca6ea4edc5a2590f45936cdda84786a7b007e
