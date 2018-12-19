from flask import Flask, render_template
from flask import Markup

app_thr = Flask(__name__)

STUDENT = {'name': '张三', 'age': 20, 'gender': '男'},

STUDENT_LIST = [
    {'name': '李四', 'age': 21, 'gender': '男'},
    {'name': '小美', 'age': 22, 'gender': '女'},
    {'name': '王五', 'age': 23, 'gender': '男'}
]

STUDENT_DICT = {
    1: {'name': '李四', 'age': 21, 'gender': '男'},
    2: {'name': '小美', 'age': 22, 'gender': '女'},
    3: {'name': '王五', 'age': 23, 'gender': '男'}
}


@app_thr.route('/student')
def student():
    return render_template('student.html', stu=STUDENT)


@app_thr.route('/student_list')
def student_list():
    return render_template('student_list.html', stu_list=STUDENT_LIST)


@app_thr.route('/student_dict')
def student_dict():
    return render_template('student_dict.html', stu_dict=STUDENT_DICT)


@app_thr.route('/student_all')
def student_all():
    return render_template('student_all.html',
                           stu=STUDENT,
                           stu_list=STUDENT_LIST,
                           stu_dict=STUDENT_DICT)


@app_thr.route('/one')
def one():
    tag = "<h1>这是从后端返回的代码效果</h1>"
    return render_template('one.html', tag=tag)


@app_thr.route('/two')
def two():
    tag = "<h1>这是从后端返回的代码效果</h1>"
    markup_tag = Markup(tag)
    print(markup_tag)  # <h1>这是从后端返回的代码效果</h1>
    print(type(markup_tag))  # <class 'markupsafe.Markup'>
    return render_template("two.html", tag=markup_tag)


def sum_demo(a, b):
    return int(a + b)


@app_thr.route('/sum_demo')
def sum_demo():
    return render_template('sum_demo.html', tag=sum_demo)


if __name__ == '__main__':
    app_thr.run('127.0.0.1', 5003, debug=True)
