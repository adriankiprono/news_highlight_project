from flask import render_template
from app import app
from .request import get_source

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


@app.route('/source/<source_id>')
def source(source_id):


    '''
    View movie page function that returns the source details page and its data
    '''
    return render_template('source.html',id = source_id)
