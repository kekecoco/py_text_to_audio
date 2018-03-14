# -*- coding: utf-8 -*-
# @author Wu Lihua
# @email maikekechn@gmail.com

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'index'

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)




