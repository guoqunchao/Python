from flask import Flask,views,jsonify,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


# app.add_url_rule方法
"""@app.route装饰器；等同于 app.add_url_rule('/list/',endpoint='list_page',view_func=list)"""
@app.route('/list/')
def list():
    return "我是列表页"


# 标准类视图
class ClassView(views.View):
    """
    1.必须继承'flask.views.Views'
    2.必须实现'dispatch_request'方法。
    3.必须通过'app.add_url_rule(rule,endpoint,view_func)'来做url与视图的映射，'view_func'这个参数必须使用类视图下的'as_view'类方法转换。
    """
    def dispatch_request(self):
        return "class view"
app.add_url_rule('/class/',endpoint='class',view_func=ClassView.as_view('class'))


# 类视图案例1
class JsonView(views.View):
    """定义Json类方法，调用返回Json数据"""
    def dispatch_request(self):
        return jsonify(self.get_data())
class ExampleView(JsonView):
    def get_data(self):
        return {'username':'zhiliao','password':'111111'}
app.add_url_rule('/example/',endpoint='ExampleView',view_func=ExampleView.as_view('ExampleView'))


# 类视图案例2
class ADSView(views.View):
    def __init__(self):
        super(ADSView, self).__init__()
        self.content = {
            'ads':'今年过节不收礼！'
        }
class LoginView(ADSView):
    def dispatch_request(self):
        self.content.update({"ads":"aaaaaaa"})    # 自定义修改各自数据,比较方便
        return render_template('login.html',**self.content)
class RegistView(ADSView):
    def dispatch_request(self):
        return render_template('regist.html',**self.content)
app.add_url_rule('/login/',view_func=LoginView.as_view('login'))
app.add_url_rule('/regist/',view_func=RegistView.as_view('regist'))


if __name__ == '__main__':
    app.run(debug=True,port=80)