# -*- coding: utf-8 -*-
# @author Wu Lihua
# @email maikekechn@gmail.com

from flask import Blueprint
from db.mysql_client import Account

login_bp = Blueprint('login', __name__)


@login_bp.route('/login')


def index():
	return '<h3>登录</h3>'

