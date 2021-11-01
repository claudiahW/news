from flask import render_template
from app import app
from .request import get_news 
# Views
@app.route('/')
def index():
    '''
    View news page function that returns the index page and its data
    '''
    #getting latest news
    latest_news =get_news('latest')
    upcoming_news = get_news('upcoming')
    print(latest_news)

    title = 'Home - Welcome to The best news site Online'
    return render_template('index.html', title = title , latest =latest_news ,upcoming = upcoming_news)

@app.route('/news/<news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)   

