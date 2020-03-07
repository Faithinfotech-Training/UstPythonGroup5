from flask import Flask
from app_package.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_pymongo import PyMongo
<<<<<<< HEAD
from flask_login import LoginManager
=======
from app_package.config import Config
>>>>>>> a12a5af579bec886d5c34a22f8cec70f8edf3e2f

app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate=Migrate(app,db)
mongo=PyMongo(app)
<<<<<<< HEAD
login_manager=LoginManager(app)
login_manager.login_view="index"

from app_package import models,routes
=======



#login_manager=LoginManager(app)
#login_manager.login_view="index"

from app_package import resource_routes,batchroutes,courseroutes
>>>>>>> a12a5af579bec886d5c34a22f8cec70f8edf3e2f
