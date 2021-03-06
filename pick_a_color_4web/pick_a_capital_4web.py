 # -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='欢迎来到网上选首都！')

@app.route('/pick_a_capital', methods=['POST'])
def pick_a_capital() -> 'html':
    """提取用户web 请求POST方法提交的数据（输入），不执行任何动作（处理），直接返回（输出）。"""
    user_capital = request.form['user_capital']	
    return render_template('results.html',
                           the_title = '以下是您选取的手都：',
                           the_capital = user_capital,
                           )

if __name__ == '__main__':
    app.run(debug=True)
