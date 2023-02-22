from bottle import *
from bottle import template

app = Bottle()

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/')
def index():
    return "Welcome to my website!"

@app.route('/about')
def about():
    return "About me"

@app.route('/linux/<name>')
def hello(name):
    title = "Hello " + name
    message = "dans linux"
    return template('template', title=title, message=message)


run(app, host='localhost', port=8080)