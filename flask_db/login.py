from flask import Flask, request, render_template, redirect
from flask import views
from wtforms.fields import simple, core
from wtforms import Form
from wtforms import validators


class LoginFrom(Form):
    username = simple.StringField(
        label="账号",
        validators=[
            validators.DataRequired(message="用户名不能为空"),
            validators.Length(min=8, max=16, message="账号长度需介于8-16字符之间")
        ],
        render_kw={"class": "my_username"}
    )

    password = simple.PasswordField(
        label="密码",
        validators=[
            validators.DataRequired(message="用户名不能为空"),
            validators.Length(min=6, max=6, message="密码必须为6位数字"),
            validators.Regexp(regex="\d+", message="密码必须为数字")
        ],
        render_kw={"class": "my_password"}
    )


login_app = Flask(__name__)  # 实例化Flask对象


@login_app.route('/home')  # FBV写的测试页面
def home_page():
    return "This is home page"


class LoginClass(views.MethodView):  # 登录类
    def get(self):  # 网站GET请求
        login_form = LoginFrom()  # 实例化LoginForm
        return render_template('login.html', login_form=login_form)  # 返回注册网页页面

    def post(self):  # 网站POST请求
        login_form = LoginFrom(request.form)  # 实例化LoginForm
        if login_form.validate():  # 校验合法
            return redirect('/home')  # 返回home测试页面
        else:
            return render_template('login.html', login_form=login_form)  # 不合法留在登


class RegFrom(Form):
    username = simple.StringField(
        label="账号",
        validators=[
            validators.DataRequired(message="账号不能为空"),
            validators.Length(min=8, max=16, message="账号长度在8-16位之间")
        ],
        render_kw={"class": "my_username"}
    )

    password = simple.PasswordField(
        label="密码",
        validators=[
            validators.DataRequired(message="密码不能为空"),
            validators.Length(min=6, max=6, message="密码长度为6位"),
            validators.Regexp(regex='\d+', message="密码必须为数字")
        ],
        render_kw={"class": "my_password"}
    )

    re_password = simple.PasswordField(
        label="确认密码",
        validators=[
            validators.EqualTo(fieldname="password", message="两次密码不一致")
        ]
    )

    email = simple.StringField(
        label="邮箱",
        validators=[
            validators.Email(message="格式不正确")
        ],
        render_kw={"class": "my_email"}
    )

    nickname = simple.StringField(
        label="昵称",
        validators=[
            validators.DataRequired(message="密码不能为空"),
        ],
        render_kw={"class": "my_nickname"}
    )

    gender = core.RadioField(
        label="性别",
        coerce=int,
        choices=(
            (1, "M"),
            (2, "F")
        ),
        default=1
    )

    hobby = core.SelectMultipleField(
        label="爱好",
        coerce=int,
        choices=(
            (1, "Apple"),
            (2, "Sumsung"),
            (3, "Mi"),
            (4, "Meizu"),
            (5, "Huawei"),
            (6, "Nubia")
        ),
        default=(1, 2, 3)
    )


class RegClass(views.MethodView):
    def get(self):
        reg_form = RegFrom()
        return render_template('reg.html', reg_form=reg_form)

    def post(self):
        reg_form = RegFrom(request.form)
        if reg_form.validate():
            return redirect('/login')
        else:
            return render_template('reg.html', reg_form=reg_form)


login_app.add_url_rule('/login', view_func=LoginClass.as_view('login'))
login_app.add_url_rule('/reg', view_func=RegClass.as_view('reg'))

if __name__ == '__main__':
    login_app.run('0.0.0.0', 4567, debug=True)  # 运行
