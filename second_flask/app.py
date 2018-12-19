from flask import Flask
from flask import request
from flask import render_template
from flask import redirect

USER = {"username": "Aibentao", "password": "aibentao123"}

STUDENT_DICT = {
    1: {"name": "one", "age": 18, "gender": "Male"},
    2: {"name": "two", "age": 19, "gender": "Female"},
    3: {"name": "thr", "age": 20, "gender": "Male"}
}

app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == USER["username"] and request.form["password"] == USER["password"]:
            return redirect("/student_list")
        return render_template("login.html", msg="用户名或者密码错误")
    return render_template("login.html", msg=None)


@app.route("/student_list")
def student_list():
    return render_template("student_list.html", stu=STUDENT_DICT)


@app.route("/student_info")
def student_info():
    stu_id = int(request.args["id"])
    stu_info = STUDENT_DICT[stu_id]
    return render_template("student_info.html", stu_info=stu_info, stu_id=stu_id)


if __name__ == '__main__':
    app.run("127.0.0.1", 6001, debug=True)  # chrome无法使用6000端口哦
