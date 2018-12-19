from flask import Flask, request, render_template

app_two = Flask(__name__)


@app_two.route('/req', methods=['POST','GET'])
def req():
    if request.method == 'GET':
        return render_template('req.html')
    else:
        print(request.method)
        print(request.form)
        print(request.form['username'])
        print(request.form.get('password'))
        print(request.form.keys())
        return "OK"


if __name__ == '__main__':
    app_two.run('127.0.0.1', 5002, debug=True)
