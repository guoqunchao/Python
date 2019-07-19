from flask import Blueprint

userBP = Blueprint('user',__name__,url_prefix='/user')

@userBP.route('/profile/')
def user_profile():
    return "个人用户中心"

@userBP.route('/settings/')
def user_setting():
    return "个人配置中心"


