# Flask这个类是项目的核心，以后很多操作都是基于这个类的对象
from flask import Flask,request,url_for,redirect,render_template,Response,jsonify
import config
import uuid
from werkzeug.routing import BaseConverter
print(uuid.uuid4())

# 创建一个Flask对象，传递__name__参数进去，以后一些Flask插件，比如Flask-migrate、Flask-SQLAlchemy如果报错，那么Flask可以通过这个参数找到具体的位置
app = Flask(__name__)

# 装饰器，将url中的/映射到hello_world这个视图函数上面，执行函数，将函数的返回值返回浏览器
@app.route('/')
def hello_world():
    print(url_for('posts',boards=['a','b']))
    return 'Hello World!'

# Config笔记
# app.config.from_object(config) | app.config.from_pyfile('config.py')

# 传递参数语法为<参数名>; 指定参数类型 string、int、float、path、uuid、any等;path接收多个路径;默认数据类型为string;
@app.route('/p/<int:id>/')
def detail_id(id):
    return '您请求的文章是: %s' %id

# 只能接收符合uuid的字符串，为全球唯一,否则报错404
@app.route('/u/<uuid:user_id>/')
def user_detail(user_id):
    return '用户个人中心：%s' %user_id

# /user/id  |  /blog/id
@app.route('/<any(blog,user):url_path>/<id>/')
def detail(url_path,id):
    if url_path == 'blog':
        return "博客详情 %s" %id
    elif url_path == 'user':
        return "用户详情 %s" %id

# 使用查询字符串的方式，通过?key=value的形式传递; http://127.0.0.1/d/?wd=e173bfa3-f840-4044-8ed7-790764cd42
@app.route('/d/')
def d():
    wd = request.args.get('wd')
    return "您通过查询字符串的方式传递的参数是：%s" %wd

# url_for 翻转url；第一个参数为视图函数的名字的字符串，后面的参数就是传递给url；如果传递的参数之前已经定义，那这个参数会便为path的形式给url，否则以查询字符串的方式传递；
@app.route('/url_for/')
def url():
    return url_for('detail',url_path='blog',id=1)

# 自定义URL转换器；to_python方法的返回值，会传递到view视图函数作为参数；
class TelephoneConverter(BaseConverter):
    regex = r'1[85734]\d{9}'
app.url_map.converters['tel'] = TelephoneConverter
@app.route('/telephone/<tel:my_tel>/')
def my_tel(my_tel):
    return "您的手机号码是：%s" %my_tel

# 自定义URL转换器；to_python方法的返回值，会传递到view视图函数作为参数；
# 自定义URL转换器；to_url方法的返回值，会在调用url_for函数的时候生成符合要求的URL形式；
class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split('+')

    def to_url(self, value):
        return "+".join(value)

app.url_map.converters['list'] = ListConverter
@app.route('/posts/<list:boards>/')
def posts(boards):
    return "您提交的列表为: %s" %boards

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)