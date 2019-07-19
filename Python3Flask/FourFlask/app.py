from flask import Flask,render_template,views,request

app = Flask(__name__)


class LoginView(views.MethodView):
    def get(self,error_msg=None):
        return render_template('index.html',error_msg=error_msg)
    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == '111111':
            return render_template('home.html')
        else:
            return self.get(error_msg="用户名或密码错误!")
app.add_url_rule('/',endpoint='LoginView',view_func=LoginView.as_view('LoginView'))


if __name__ == '__main__':
    app.run(debug=True,port=80)
