from flask import Flask, jsonify, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, or_
from flask_cors import CORS
import traceback

from werkzeug.security import check_password_hash, generate_password_hash
import jwt
from functools import wraps
from datetime import datetime, timedelta


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:password@localhost:5432/todolist"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)
