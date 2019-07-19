from flask import Blueprint,redirect,url_for

newsBP = Blueprint('news',__name__,url_prefix='/new')

@newsBP.route('/list/')
def news_list():
    return "新闻列表页面"

@newsBP.route('/detail/')
def news_detail():
    return "新闻详情页面"