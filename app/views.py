# Views
@app.route('news')
def movie(news):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('index.html')

def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best News Website Online'
    return render_template('index.html', title = title)
