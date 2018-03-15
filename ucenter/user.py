# -*- coding: utf-8 -*-
# @author Wu Lihua
# @email maikekechn@gmail.com

from flask import Flask, Blueprint

user_bp = Blueprint('ucenter', __name__)

@user_bp.route('/user')
def index():
	return '<h3>用户中心</h3>'