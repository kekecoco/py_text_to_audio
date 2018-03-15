# -*- coding: utf-8 -*-
# @author Wu Lihua
# @email maikekechn@gmail.com

from flask import Flask
from login.login import login_bp
from login.logout import logout_bp
from ucenter.user import user_bp

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(user_bp)

@app.route('/')
def index():
	return 'index'

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)




