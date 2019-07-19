from flask import Flask,Blueprint,render_template
from BluePrint.news import newsBP
from BluePrint.users import userBP

app = Flask(__name__)
app.register_blueprint(userBP)
app.register_blueprint(newsBP)

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True,port=80)
