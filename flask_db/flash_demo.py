from flask import Flask, request, render_template, redirect, url_for, flash, get_flashed_messages
from flask import views

app = Flask(__name__)
app.secret_key = 'Hello'


@app.route('/')
def index():
    flash('one', 'two')
    flash('thr', 'fou')
    flash('fiv', 'six')
    return "This is index"


class LoginClass(views.MethodView):
    def get(self):
        print(get_flashed_messages('two'))
        print(get_flashed_messages('fou'))
        print(get_flashed_messages('six'))
        return "LoginClass GET"

    def post(self):
        return "LoginClass POST"


app.add_url_rule('/login', view_func=LoginClass.as_view('login'))


@app.before_first_request
def bfr():
    return "BFR"


if __name__ == '__main__':
    app.run(debug=True)
