from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = 'Hello World'
    title = 'this is the internationsl news department'

    return render_template('index.html', title = title)


@app.route('/source/<source_id>')
def source(source_id):


    '''
    View movie page function that returns the source details page and its data
    '''
    return render_template('source.html',id = source_id)
