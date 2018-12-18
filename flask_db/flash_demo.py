from flask import Flask, request, render_template, redirect, url_for, flash, get_flashed_messages
from flask import views

app = Flask(__name__)
app.secret_key = 'Hello'


@app.route('/')
def index():
    return "This is index"


class LoginClass(views.MethodView):
    def get(self):
        return render_template('login.html')

    def post(self):
        return "POST"
