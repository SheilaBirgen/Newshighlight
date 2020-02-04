from flask import render_template, url_for, request
from . import main
from ..requests import fetch_news,fetch_articles

# Views
@main.route('/')
def index():
    """
    Run the unit tests.
    """
    sports = fetch_news('sports')
    health = fetch_news('health')
    business = fetch_news('business')
    technology = fetch_news('technology')
    entertainment = fetch_news('entertainment')
    general = fetch_news('general')
    title="Welcome to the World's Best News Hub"

    return render_template('index.html', title=title,sports=sports, health=health, business=business, technology=technology, entertainment=entertainment, general=general) 

@main.route('/news/<int:id>')
def news(id):
    
    article_news = fetch_articles(id)
    
    return render_template('news.html',highlight_param=highlight_args,news=article_news)

@main.route('/sources/<category>')
def insdrt(category):

    sports = fetch_news('sports')
    health = fetch_news('health')
    business = fetch_news('business')
    technology = fetch_news('technology')
    entertainment = fetch_news('entertainment')
    general = fetch_news('general')
    title="Welcome to the World's Best News Hub"

    return render_template('sources.html', title=title,sports=sports, health=health, business=business, technology=technology, entertainment=entertainment, general=general)  