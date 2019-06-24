from flask import render_template
from app import app
from ..request import get_sources, get_article

@app.route('/')
#define view function
def index():
  """
  view root page function that returns index page 
  """
  sources = get_sources()
  Article = get_article()
  print(sources)
  title = 'News Highlights'
  return render_template('index.html', title = title, sources = sources, Article = Article)