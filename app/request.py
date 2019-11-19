from app import app
import urllib.request,json
from .models import source
Source =source.Source


# Getting api key
api_key = app.config['SOURCE_API_KEY']

# Getting the movie base url
base_url = app.config["SOURCE_API_BASE_URL"]

def get_source(category):

    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list=get_source_response['sources']
            source_results =process_sources(source_results_list)


    return source_results

def process_sources(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain sources details

    Returns :
        source_results: A list of sources objects

    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')
        
        new_object = Source(id,name,description,url,category,language,country)
        source_results.append(new_object)


    return source_results

def get_articles(id):
    get_articles_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data) 

        articles_results = None
        if articles_response:
            id=articles_response.get(id)
            name=articles_response.get(name)
            author = articles_response.get(author)
            description = articles_response.get(description)
            url = articles_response.get(url)
            urlToImage = articles_response.get(urlToImage) 
            publishedAt = articles_response.get(publishedAt)

            articles_results=Articles(id,name,author,description,url,urlToImage,publishedAt)
        return articles_results

        

            




                


