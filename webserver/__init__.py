from flask import Flask, render_template, url_for
import mysql.connector


server = Flask(__name__)
server.config['SECRET_KEY'] = "ATMOSTSECURE"


db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="resume_db"
)

from .views import views
server.register_blueprint(views, url_prefix="/")