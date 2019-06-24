from app import app
import urllib.request, json
from .models import Newssource

Newssource = newssource.Newssource
#api key
api_key = app.config['NEWS_API_KEY']

#base url
base_url = app.config['NEWS_API_BASE_URL']

def get_sources():
  """
  gets the json response to our url request
  """
  get_sources_url = base_url.format(api_key)
  
  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)
    
    sources_results = None
    if get_sources_response['results']:
      sources_results_list = get_sources_response['results']
      sources_results = process_results(sources_results_list)
      
  return sources_results
def process_results(sources_list):
  """
  processes sources result and transform them to a list of objects
  """
  sources_results = []
  for source_item in sources_list:
    id = source_item.get('id')
    name = source_item.get('name')
    description = source_item.get('description')
    url = source_item.get('url')
    
    source_object = Newssource(id, name, description, url)
    sources_results.append(source_object)
  return sources_results