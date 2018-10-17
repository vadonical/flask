from flask import Flask, url_for, request, render_template  # 导入Flask类

app = Flask(__name__)  # 创建类的实例


@app.route('/')  # 使用 route() 装饰器来告诉 Flask 触发函数的 URL
def hello_world():
    return 'Hello World!'  # 返回浏览器中的信息


@app.route('/index')  # 定义index路由
def index():
    return 'This is index!'  # 返回浏览器中的信息


@app.route('/user/<username>')
def show_username(username):
    return 'User is %s!' % username


@app.route('/post/<int:post_id>')
def show_post_id(post_id):
    return 'Post_id is %d!' % post_id


@app.route('/path/<path:sub_path>')
def show_path(sub_path):
    return 'Sub_path is %s' % sub_path


@app.route('/project/')
def project():
    return 'This is project!'


@app.route('/about')
def about():
    return 'This is about!'


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if login_success(request.form['username'], request.form['password']):
            return login_with_user(request.form['username'])
        else:
            error = 'Invalid username or password!'
    return render_template('login.html', error=error)


@app.route('/person/<name>')
def show_name(name):
    return 'Your name is %s' % name


with app.test_request_context():
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('show_name', name='john'))

with app.test_request_context('/one', method='POST'):
    assert request.path == '/one'
    assert request.method == 'POST'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return 'This is POST!'
    elif request.method == 'GET':
        return 'This is GET!'
    else:
        return 'ERROR!'


@app.route('/show_templates/')
@app.route('/show_templates/<name>')
def show_templates(name=None):
    return render_template('one.html', name=name)


if __name__ == '__main__':
    app.run()  # 执行
