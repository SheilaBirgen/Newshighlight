class News:
    '''
    news class to define news Objects
    '''

    def __init__(self,id, name,category,description,url,country):
        self.id =id
        self.name= name
        self.category=category
        self.description = description
        self.url= url
        self.country=country

class Articles:
    """
    Defines what our articles object will look like
    """

    def __init__(self,id,name,author,title,description,url,urlToImage,publishedAt):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt