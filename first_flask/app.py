from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/')
def index():
    return 'This is Index Page!'


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/reg')
def reg():
    return redirect('/login')


@app.route('/info')
def info():
    return render_template('info.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9527, debug=True)
