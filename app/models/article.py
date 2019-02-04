class Article:
    '''
    Article class to define article Objects
    '''

    def __init__(self,id,name,author,title,url,publishedAt):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.url= 'https://www.forbes.com/sites/billybambrough/2019/02/04/twitter-ceo-jack-dorsey-has-made-a-bold-prediction-about-bitcoin/'
        self.publishedAt = publishedAt
