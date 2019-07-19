from flask import Flask,url_for,Response,jsonify,render_template

app = Flask(__name__)

class JsonResponse(Response):

    @classmethod
    def force_type(cls, response, environ=None):
        '''
        这个方法只有视图函数返回非字符、非元祖、非Response对象才会调用
        :param response:
        :param environ:
        :return:
        '''
        #把字典转换成json
        if isinstance(response,dict):
            #jsonify将字典转换成json对象，还将该对象包装成了一个Response对象
            response = jsonify(response)
        return super(JsonResponse, cls).force_type(response,environ)

app.response_class = JsonResponse

@app.route('/')
def hello_world():
    content = {
        # 'signature':"我就是我，不一样的烟火！",
        'signature':None,
        'render':'1',
    }
    return render_template('index.html',**content)

@app.route('/list1/')
def list1():
    return Response('list1')  #合法对象，直接返回

@app.route('/list2/')
def list2():
    return {'username':'derek','age':18}   #返回的是非字符、非元祖、非Response对象，所以执行force_type方法

@app.route('/account/login/<id>/')
def login(id):
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)