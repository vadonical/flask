# Flask 模板
- 本次模板基于Flask1.0
## 最小的app
- 一个最小的Flask应用如下
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
        - project 的 URL 是中规中举的，尾部有一个斜杠，看起来就如同一个文件夹。 访问一个没有斜杠结尾的 URL 时 Flask 会自动进行重定向，帮你在尾部加上一个斜杠。
        - about 的 URL 没有尾部斜杠，因此其行为表现与一个文件类似。如果访问这个 URL 时添加了尾部斜杠就会得到一个 404 错误。这样可以保持 URL 唯一，并帮助 搜索引擎避免重复索引同一页面。

### URL 创建
- url_for() 函数用于构建指定函数的 URL。它把函数名称作为第一个 参数。它可以接受任意个关键字参数，每个关键字参数对应 URL 中的变量。未知变量 将添加到 URL 中作为查询参数。
    - **QUESTIONS:**为什么不在把 URL 写死在模板中，而要使用反转函数 url_for() 动态构建？
        - 反转通常比硬编码 URL 的描述性更好。
        - 你可以只在一个地方改变 URL ，而不用到处乱找。
        - URL 创建会为你处理特殊字符的转义和 Unicode 数据，比较直观。
        - 生产的路径总是绝对路径，可以避免相对路径产生副作用。
        - 如果你的应用是放在 URL 根路径之外的地方（如在 /myapplication 中，不在 / 中）， url_for() 会为你妥善处理。





