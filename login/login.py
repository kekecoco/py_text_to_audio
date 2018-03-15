# -*- coding: utf-8 -*-
# @author Wu Lihua
# @email maikekechn@gmail.com

from flask import Flask, Blueprint

login_bp = Blueprint('login', __name__)

@login_bp.route('/')
def index():
	return '<h3>login</h3>'