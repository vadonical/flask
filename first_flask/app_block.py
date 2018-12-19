from flask import Flask, render_template

app_block = Flask(__name__, template_folder='temp')


@app_block.route('/login')
def login():
    return render_template('login.html')


@app_block.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app_block.run('127.0.0.1', 5004, debug=True)
