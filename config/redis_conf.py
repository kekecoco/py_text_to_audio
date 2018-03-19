# -*- coding: utf-8 -*-
# @author Wu Lihua
# @email maikekechn@gmail.com

from config.base_conf import import_config


def import_redis_config(app_conf_name):
    return import_config('../config/redis.conf', app_conf_name)
