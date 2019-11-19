from flask import render_template
from app import app
from .request import get_source,get_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'this is the internationsl news department'
    #Getting the source
    sports_source=get_source('sports')
    business_source=get_source('business')
    entertainment_source=get_source('entertainment')
    technology_source =get_source('technology')
    # politics_source= get_source('politics')
    

    return render_template('index.html', title = title,sports = sports_source ,business=business_source,entertainment=entertainment_source,technology=technology_source)


@app.route('/articles')
def articles(articles_id):


    '''
    View movie page function that returns the news articles page and its data
    '''
    return render_template('articles.html',id = articles_id)
