# -*- coding: utf-8 -*-
# @author Wu Lihua
# @email maikekechn@gmail.com

from config.base_conf import import_config


def import_mysql_config(app_conf_name):
    return import_config('../config/mysql.conf', app_conf_name)

