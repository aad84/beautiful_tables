from flask import Flask, flash, redirect, render_template, \
    request, url_for
import time

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# HISTORY

history_list = []

# 主页路由
@app.route('/')
def index():
    return render_template('index.html')

# 计算器路由
@app.route('/calculate.html', methods=['GET', 'POST'])
def subtraction():
    error = None
    if request.method == 'POST':

        if len(request.form['firstNum']) == 0 or \
                len(request.form['secondNum']) == 0:
            flash('Please enter numbers !')
        else:
            #put the numbers to the list

            cal_history = {'cal_time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
            a = request.form['firstNum']
            cal_history['first_num'] = a
            b = request.form['secondNum']
            cal_history['second_num'] = b
            result = int(a) - int(b)
            cal_history['operation'] = 'Subtraction'
            cal_history['result'] = result

            # print(result)
            flash(result)
            # print(cal_history)
            history_list.append(cal_history)
            print(history_list)
            # return redirect(url_for('/calculate.html'))
    return render_template('/calculate.html', error=error)

# history路由
@app.route('/history', methods=["POST","GET"])
def history():
    if request.method == "GET":
        return render_template("/history.html", his=history_list)
