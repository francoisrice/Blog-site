import time # To set the post time as the current time

# Need to import flask_db; hopefully this tasks care of it:
from app import app

# Not sure if these are needed; might come in when importing the app
import re

app = Flask(__name__)
#db = SQLAlchemy(app) # if SQLAlchemy was being used

class Post(flask_db.Model): 
	"""The posts that will be created by the user."""
	def __init__(self, title=CharField(),slug=CharField(unique=True),content=TextField(),published=BooleanField(index=True),timestamp=DateTimeField(default=datetime.datetime.now, index=True)):
		self.title = title
		self.slug = slug
		self.content = content
		self.published = published
		self.timestamp = timestamp
		self.id = ""

	def save(self,*arg,**kwargs):
		if not self.slug:
			self.slug = re.sub("[^\w]+","-",self.title.lower())
		ret = super(Entry, self).save(*args,**kwargs)

		# Store the search content
		self.update_search_index()
		return ret

	#TODO - Continue and finish the tutorial

	def update_search_index(self):
		return True

class SearchPost(object):
	"""Object to reflect the blog post, and allow searching"""
	def __init__(self,docid="",keywords="",content=""):
		self.docid = docid
		self.keywords = keywords
		self.content = content
		pass

