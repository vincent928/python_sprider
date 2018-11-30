# -*- coding: utf-8 -*-
# @Author = moon
# @Create = 2018/4/24 13:54
# @File = demo.py


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello,world!'

if __name__ == '__main__':
    app.run()



















