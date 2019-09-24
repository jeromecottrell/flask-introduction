from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to our Library!'

@app.route('/python')
def hello_python():
    return '<h1>Python Programming Language</h1>'

@app.route('/hello/<name>')
def hello_developer(name=None):
    return 'Hello {}, how are you?'.format(name)
