# -*- coding: utf-8 -*-
# @author Wu Lihua
# @email maikekechn@gmail.com

import redis
from config import setup

# redis连接
def redis_connect():
    redis_config = setup.get_sections(setup.redis_config_file, 'redis')
    if not redis_config:
        return False

    try:
        redis_conn = redis.StrictRedis(host=redis_config['hostname'], port=redis_config['port'])
    except ConnectionAbortedError:
        return False
    else:
        return redis_conn

def set(key, value):
    pass

def get(key):
    pass

if __name__ == '__main__':
    redis_connect()