from flask import render_template
from app import app

@app.route('/')
#define view function
def index():
  """
  view root page function that returns index page 
  """
  return render_template('index.html')