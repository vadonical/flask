# Flask 初识

## 第一节 简介

首先,要看你学没学过 Django 如果学过 Django 的同学,请从头看到尾,如果没有学过 Django 的同学,并且不想学习 Django 的同学,请自觉绕过第一节。

### Python三大 Web 框架 Django Tornado Flask 主要对比

| 特点 | Django | Tornado | Flask |
| --- | --- | --- | --- |
| JSON 测试（Req/s） | 4762 | 2578 | 4630 |
| 远程处理延时（ms） | 3477.36 | 1036.97 | 3344.27 |
| 数据库与模板处理（ms） | 2904.04 | 1344.69 | 1440.24 |  
 
**各自特点**：

- Django 
    - 大而全,集成了很多组件,例如: Models、Admin、Form 等等, 不管你用得到用不到,反正它全都有,属于全能型框架。Django 通常用于大型 Web 应用由于内置组件足够强大所以使用 Django 开发可以一气呵成。缺点就是项目太庞大，开发团队执拗。

- Tornado 
    - 原生异步非阻塞,在 IO 密集型应用和多任务处理上占据绝对性的优势,属于专注型框架。通常用于 API 后端应用,游戏服务后台,其内部实现的异步非阻塞速度很快。缺点是太干净，不支持 session。

- Flask 
    - 小而轻,原生组件几乎为零，三方提供的组件非常全面,属于短小精悍型框架。通常应用于小型应用和快速构建应用,其强大的三方库，足以支撑一个大型的 Web 应用。缺点是大部分插件完全调用第三方或者需要自己写，可能造成一定的漏洞和风险。

### HelloWorld

1. 下载或导入flask包

- [app.py](app.py)

```python
from flask import Flask  # 导入Flask模块

app = Flask(__name__)  # 实例化Flask模块，__name__表示当前路径


@app.route('/hello')  # 设置路由
def hello():
    return 'Hello, World!'  # 返回字符串
    
    
app.run(host='0.0.0.0', port=9527, debug=True)
```

### Flask 中的 HttpResponse，redirect 和 render_template

- [app_one.py](app_one.py)

### Flask 中的 request

- [app_two.py](app_two.py)

每个框架中都有处理请求的机制(request),但是每个框架的处理方式和机制是不同的，为了了解 Flask 的 request 中都有什么东西，首先我们要写一个前后端的交互——基于 HTML + Flask 写一段前后端的交互查看下列代码：

methods=\['POST','GET']表示接受请求方式有两种，如果不加上次参数表示默认的 GET 请求。

关于 request 的相关属性和方法有：

- request.method
    - 表示提交的处理请求方法，可以通过该方法来拿到其请求方法参数。
    
- request.form
    - 表示传递过来的值。我们可以继续使用关键字取值或者 get 方法拿到参数。
    
- request.args
    - 表示所有的 url 参数。
    
- request.values
    - 表示所有的参数。
    
- request.cookies
    - 读取数据中的参数。
    
- request.headers
    - 表示请求头中的所有参数。
    
- request.data
    - 当某些数据无法被处理时都放在里面。
    
- request.files
    - 表示上传的文件。
    
- request.path
    - 获取当前 url 的路径。
    
- request.script_root
    - 获取当前 url 的上一级路径。
    
- request.url
    - 获取当前 url 的全部路径。
     
- request.url_root
    - 获取当前 url 的路径的上一级全部路径。


