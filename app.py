from flask import Flask  # 导入Flask类

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


if __name__ == '__main__':
    app.run()  # 执行
