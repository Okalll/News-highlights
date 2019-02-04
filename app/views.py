from flask import render_template
from app import app
from .request import get_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_article = get_articles('popular')
    business_article = get_articles('business')
    sports_article = get_articles('sports')
    entertainment_article = get_articles('entertainment')
    title = 'Home - Welcome to The best News Website'
    return render_template('article.htm', title = title, popular = popular_article, business = business_article, sports = sports_article, entertainment = entertainment_article )

def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best News Website'
    return render_template('article.htm', title = title)
