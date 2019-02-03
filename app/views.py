# Views
@app.route('news')
def movie(news):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = movie_id)
