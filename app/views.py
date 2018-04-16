from app import app # run the applcation
from flask import render_template # display webpages


@app.route('/',  methods=['GET','POST'])
def index():
	return render_template('index.html')