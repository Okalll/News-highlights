from flask import render_template
from app import app

# Views
@app.route('/article/<article_name>')
def movie(article_name):

    '''
    View article page function that returns the article details page and its data
    '''
    return render_template('article.html',name = article_name)
