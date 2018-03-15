# -*- coding: utf-8 -*-
# @author Wu Lihua
# @email maikekechn@gmail.com

from flask import Flask, Blueprint

logout_bp = Blueprint('login', __name__)

@logout_bp.route('/logout')
def index():
	return '<h3>登出</h3>'