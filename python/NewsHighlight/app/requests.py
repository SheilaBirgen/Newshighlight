import urllib.request, json
from .models import News, Articles

# Getting api key
# api_key = app.config['NEWSHIGHLIGHT_API_KEY']

# Getting the news base url
# base_url = app.config['HIGHLIGHT_API_BASE_URL']


def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWSHIGHLIGHT_API_KEY']
    base_url = app.config['HIGHLIGHT_API_BASE_URL']
   


def fetch_news(category):
    '''
    Function that gets the json response to our url request
    '''
    fetch_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(fetch_news_url) as url:
        fetch_news_data = url.read()
        fetch_news_response = json.loads(fetch_news_data)

        news_results = None

        if fetch_news_response['sources']:
            news_results_list = fetch_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):

    news_results = []
    for news in news_list:
        id = news.get('id')
        name = news.get('name')
        category = news.get('category')
        description= news.get('description')
        url= news.get('url')
        country = news.get('country')
       
        if url:
            news_object =News(id,name,category, description, url, country)
            news_results.append(news_object)

    return news_results

    

def fetch_articles(id):
    """
    Function that gets the json response to our url request
    """
    fetch_articles_url = news_url.format(id, api_key)
    with urllib.request.urlopen(fetch_articles_url) as url:
        fetch_news_data = url.read()
        fetch_news_response = json.loads(fetch_news_data)
        
        news_results = None

        if fetch_news_response['articles']:
            news_results_list = fetch_news_response['articles']
            news_results = process_articles(news_results_list)

    return news_results


def process_articles(articles_list):
   
    news_results = []
    news_dictionary= {}
    for result in articles_list:
       
        news_id = result['news']
        
        news_dictionary['id'] = news_id['id']
        news_dictionary['name'] = news_id['name']
        id = news_dictionary['id']
        name = news_dictionary['name']
        print(name)
        
        author = result.get('author')
        title = result.get('title')
        description = result.get('description')
        url = result.get('url')
        urlToImage = result.get('urlToImage')
        publishedAt = result.get('publishedAt')

        if urlToImage:
            print(id)
            news_object = Articles(id,name,author,title,description,url,urlToImage, publishedAt)
                                     
            news_results.append(news_object)

    return news_results