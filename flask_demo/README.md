# Flask 模板
- 本次模板基于 Flask 1.0
---
## 最小的 app
- 一个最小的 Flask 应用如下
    - 代码
    ```text
    from flask import Flask  # 导入Flask类
    
    app = Flask(__name__)  # 创建类的实例
    
    
    @app.route('/')  # 使用 route() 装饰器来告诉 Flask 触发函数的 URL 
    def hello_world():
        return 'Hello World!'  # 返回浏览器中的信息
    
    
    if __name__ == '__main__':
        app.run()  # 执行
    ```
    - 代码解释
        - 首先我们导入了 Flask 类。 该类的实例将会成为我们的 WSGI 应用。
        - 接着我们创建一个该类的实例。第一个参数是应用模块或者包的名称。如果你使用 一个单一模块（就像本例），那么应当使用 __name__ ，因为名称会根据这个 模块是按应用方式使用还是作为一个模块导入而发生变化（可能是 ‘__main__’ ， 也可能是实际导入的名称）。这个参数是必需的，这样 Flask 才能知道在哪里可以 找到模板和静态文件等东西。更多内容详见 Flask 文档。
        - 然后我们使用 route() 装饰器来告诉 Flask 触发函数的 URL 。
        - 函数名称被用于生成相关联的 URL 。函数最后返回需要在用户浏览器中显示的信息。
        - 右键点击运行，点击执行中的浏览地址，使用浏览器打开。这个过程我们也可以使用命令行打开。这种方式在编译器中一般不用！
        ```text
        python -m flask run # 在PowerShell中的命令
        ```
---
## 路由 URL
- 现代 web 应用都使用有意义的 URL ，这样有助于用户记忆，网页会更得到用户的青睐， 提高回头率。
- 使用 route() 装饰器来把函数绑定到 URL:
    - 代码
    ```text
    @app.route('/')  # 使用 route() 装饰器来告诉 Flask 触发函数的 URL
    def hello_world():
        return 'Hello World!'  # 返回浏览器中的信息
    
    
    @app.route('/index')  # 定义index路由
    def index():
        return 'This is index!'  # 返回浏览器中的信息
    ```
### 变量规则
- 通过把 URL 的一部分标记为 <variable_name> 就可以在 URL 中添加变量。标记的 部分会作为关键字参数传递给函数。通过使用 <converter:variable_name> ，可以 选择性的加上一个转换器，为变量指定规则。
    - 代码
    ```text
    @app.route('/user/<username>')
    def show_username(username):
        return 'User is %s!' % username
    
    
    @app.route('/post/<int:post_id>')
    def show_post_id(post_id):
        return 'Post_id is %d!' % post_id
    
    
    @app.route('/path/<path:sub_path>')
    def show_path(sub_path):
        return 'Sub_path is %s' % sub_path
    ```
- 转换器类型

| 关键字 | 说明|
| :---: | :---: |
| string | （缺省值） 接受任何不包含斜杠的文本|
| int |	接受正整数|
| float | 接受正浮点数|
| path | 类似 string ，但可以包含斜杠|
| uuid | 接受 UUID 字符串|

### 唯一的 URL / 重定向行为
- 以下两条规则的不同之处在于是否使用尾部的斜杠。
    - 代码
    ```text
    @app.route('/project/')
    def project():
        return 'This is project!'
    
    
    @app.route('/about')
    def about():
        return 'This is about!'
    ```
    - 代码说明
        - project 的 URL 是中规中矩的，尾部有一个斜杠，看起来就如同一个文件夹。 访问一个没有斜杠结尾的 URL 时 Flask 会自动进行重定向，帮你在尾部加上一个斜杠。
        - about 的 URL 没有尾部斜杠，因此其行为表现与一个文件类似。如果访问这个 URL 时添加了尾部斜杠就会得到一个 404 错误。这样可以保持 URL 唯一，并帮助 搜索引擎避免重复索引同一页面。

### URL 构建
- url_for() 函数用于构建指定函数的 URL。它把函数名称作为第一个 参数。它可以接受任意个关键字参数，每个关键字参数对应 URL 中的变量。未知变量 将添加到 URL 中作为查询参数。
- 问题:
    1. 为什么不在把 URL 写死在模板中，而要使用反转函数 url_for() 动态构建？
        - 反转通常比硬编码 URL 的描述性更好。
        - 你可以只在一个地方改变 URL ，而不用到处乱找。
        - URL 创建会为你处理特殊字符的转义和 Unicode 数据，比较直观。
        - 生产的路径总是绝对路径，可以避免相对路径产生副作用。
        - 如果你的应用是放在 URL 根路径之外的地方（如在 /myapplication 中，不在 / 中）， url_for() 会为你妥善处理。
- 这里我们使用 test_request_context() 方法来尝试使用 url_for() 。test_request_context() 告诉 Flask 正在处理一个请求，而实际上也许我们正处在交互 Python shell 之中， 并没有真正的请求。
    - 代码
    ```text
    from flask import url_for
  
    @app.route('/login')
    def login():
        return 'login'
    
    
    @app.route('/person/<name>')
    def show_name(name):
        return 'Your name is %s' % name
    
    
    with app.test_request_context():
        print(url_for('login'))
        print(url_for('login', next='/'))
        print(url_for('show_name', name='john'))
    ```
    - 结果
    ```text
    /login
    /login?next=%2F
    /person/john
    ```
---        
## HTTP 方法
- Web 应用使用不同的 HTTP 方法处理 URL 。当你使用 Flask 时，应当熟悉 HTTP 方法。 缺省情况下，一个路由只回应 GET 请求。 可以使用 route() 装饰器的 methods 参数来处理不同的 HTTP 方法:
    - 代码
    ```text
    from flask import request
  
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            return 'This is POST!'
        elif request.method == 'GET':
            return 'This is GET!'
        else:
            return 'ERROR!'
    ```
- 如果当前使用了 GET 方法， Flask 会自动添加 HEAD 方法支持，并且同时还会 按照 [HTTP RFC](https://www.ietf.org/rfc/rfc2068.txt) 来处理 HEAD 请求。同样， OPTIONS 也会自动实现。
---
## 静态文件
- 动态的 web 应用也需要静态文件，一般是 CSS 和 JavaScript 文件。理想情况下你的 服务器已经配置好了为你的提供静态文件的服务。但是在开发过程中， Flask 也能做好 这项工作。只要在你的包或模块旁边创建一个名为 static 的文件夹就行了。 静态文件位于应用的 /static 中。
    - 使用特定的 'static' 端点就可以生成相应的 URL。如：
    ```text
    url_for('static', filename='style.css')
    ```
    - 这个静态文件在文件系统中的位置应该是 static/style.css 。
---
## 渲染模板
- 在 Python 内部生成 HTML 不好玩，且相当笨拙。因为你必须自己负责 HTML 转义， 以确保应用的安全。因此，Flask 自动为你配置 Jinja2 模板引擎。
- 使用 render_template() 方法可以渲染模板，你只要提供模板名称和需要 作为参数传递给模板的变量就行了。
    - 代码
    ```text
    from flask import render_template
    @app.route('/show_templates/')
    @app.route('/show_templates/<name>')
    def show_templates(name=None):
        return render_template('one.html', name=name)
    ```
    - Flask 会在templates文件夹中寻找模板。因此，如果你的应用应该是一个模块，那么模板文件夹应该在模块旁边；如果是一个包，那么就应该在包里面。
- 更多信息您可以访问 [Jinja2 模板官方文档](http://jinja.pocoo.org/docs/2.10/templates/)
- one.html
```html
{% if name %}
    <h1>hello,{{ name }}!</h1>
{% else %}
    <h1>Hello,World!</h1>
{% endif %}
```
- 关于模板语言，详见本人github之Django系列！
---
## 操作请求数据
- 对于 web 应用来说对客户端向服务器发送的数据作出响应很重要。在 Flask 中由全局对象 request 来提供请求信息。如果你有一些 Python 基础，那么你可能会奇怪：既然这个对象是全局的，怎么还能保持线程安全？答案是本地环境：
### 本地环境
- 某些对象在 Flask 中是全局对象，但不是通常意义下的全局对象。这些对象实际上是特定环境下本地对象的代理，还是很容易理解的。
- 设想现在处于处理线程的环境中。一个请求进来了，服务器决定生成一个新线程（或者叫其他什么名称的东西，这个下层的东西能够处理包括线程在内的并发系统）。当 Flask 开始其内部请求处理时会把当前线程作为活动环境，并把当前应用和 WSGI 环境绑定到这个环境（线程）。它以一种聪明的方式使得一个应用可以在不中断的情况下调用另一个应用。
- 这对你有什么用？基本上你可以完全不必理会。这个只有在做单元测试时才有用。在测试时会遇到由于没有请求对象而导致依赖于请求的代码会突然崩溃的情况。对策是自己创建一个请求对象并绑定到环境。最简单的单元测试解决方案是使用 test_request_context() 环境管理器。通过使用 with 语句可以绑定一个测试请求，以便于交互。例如:
```text
from flask import request

with app.test_request_context('/one', method='POST'):
    assert request.path == '/one'
    assert request.method == 'POST'
```
- 或者你也可以将整个 WSGI 环境传递给 request_context() 方法：
```text
from flask import request

with app.request_context(environ):
    assert request.method == 'POST'
```
### 请求对象
- 请求对象在 API 一节中有详细说明这里不细谈（参见 [Request](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Request) ）。 这里简略地谈一下最常见的操作。首先，你必须从 flask 模块导入请求对象:
```text
from flask import request
```
- 通过使用 method 属性可以操作当前请求方法，通过使用 form 属性处理表单数据（在 POST 或者 PUT 请求 中传输的数据）。以下是使用上述两个属性的例子:

```text
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if login_success(request.form['username'], request.form['password']):
            return login_with_user(request.form['username'])
        else:
            error = 'Invalid username or password!'
    return render_template('login.html', error=error)
```
- 当 form 属性中不存在这个键时会发生什么？会引发一个 KeyError 。如果你不像捕捉一个标准错误一样捕捉 KeyError ，那么会显示一个 HTTP 400 Bad Request 错误页面。因此，多数情况下你不必处理这个问题。
- 要操作 URL（如 ?key=value）中提交的参数可以使用 args 属性:
```text
searchword = request.args.get('key', '')
```
- 用户可能会改变 URL 导致出现一个 400 请求出错页面，这样降低了用户友好度。因此，我们推荐使用 get 或通过捕捉 KeyError 来访问 URL 参数。
- 完整的请求对象方法和属性参见 [Request](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Request) 文档。
---
## 文件上传
- 用 Flask 处理文件上传很容易，只要确保不要忘记在你的 HTML 表单中设置 enctype="multipart/form-data" 属性就可以了。否则浏览器将不会传送你的文件。
- 已上传的文件被储存在内存或文件系统的临时位置。你可以通过请求对象 files 属性来访问上传的文件。每个上传的文件都储存在这个字典型属性中。这个属性基本和标准 Python file 对象一样，另外多出一个 用于把上传文件保存到服务器的文件系统中的 save() 方法。
```text
from flask import request

@app.route('/upload', method=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        f = request.files['file_name']
        f.save(r'E:\flask_demo\file_name.txt')
        ...
```
如果想要知道文件上传之前其在客户端系统中的名称，可以使用 filename 属性。但是请牢记这个值是 可以伪造的，永远不要信任这个值。如果想要把客户端的文件名作为服务器上的文件名，可以通过 Werkzeug 提供的 secure_filename() 函数:














































