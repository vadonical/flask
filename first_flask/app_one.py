from flask import Flask, redirect, render_template

app_one = Flask(__name__)


@app_one.route('/one')
def one():
    return "Hello, this is HttpResponse!"  # HttpResponse


@app_one.route('/two')
def two():
    return redirect('/one')  # redirect


@app_one.route('/thr')
def thr():
    return render_template('thr.html')  # render_template


if __name__ == '__main__':
    app_one.run('127.0.0.1', 5001, debug=True)
