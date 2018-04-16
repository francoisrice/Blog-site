import datetime # Why?
import functools # Why?
import os # gives application path & directory
import re # Why?
import urllib # Why?

from flask import Flask, # Why?
                  abort, # Why?
                  flash, # Why?
                  Markup, # Why?
                  redirect, # Why?
                  render_template, # Why?
                  request, # Why?
                  Response, # Why?
                  session, # Why?
                  url_for # Why?

from markdown import markdown # Why?
from markdown.extensions.codehilite import CodeHiliteExtension # Why?
from markdown.extensions.extra import ExtraExtension # Why?
from micawber import bootstrap_basic, # Why?
                     parse_html # To turn embedded HTML into videos
from micawber.cache import Cache as OEmbedCache # Why?
import peewee # Why?
from playhouse.flask_utils import FlaskDB, # Why?
                                  get_object_or_404, # Why?
                                  object_list # Why?
import playhouse.sqlite_ext # Why?

ADMIN_PASSWORD = "BrittanyRocks!" # using plaintext is ok for testing, 
								  # but for deployment one-way hashes 
								  # should be used to store the password
								   
APP_DIR = os.path.dirname(os.path.realpath(__file__))
DATABASE = "sqliteext://%s" % os.path.join(APP_DIR, "blog.db")
DEBUG = False
SECRET_KEY = "secret ninja stealth key" # Used by Flask to encrypt the session cookie
SITE_WIDTH = 800


app = Flask(__name__)
app.config.from_object(__name__)

flask_db = FlaskDB(app)
database = flask_db.database

oembed_providers = bootstrap_basic(OEmbedCache())

from app import views