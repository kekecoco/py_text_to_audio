# -*- coding: utf-8 -*-
# @author Wu Lihua
# @email maikekechn@gmail.com

import redis
from config import setup

# redis连接
class redisclient:

    redis_config = None
    redis_conn = None

    def __init__(self):
        self.redis_config = setup.get_sections(setup.redis_config_file, 'redis')

        try:
            redis.StrictRedis(host=self.redis_config['hostname'], port=self.redis_config['port'])
        except ConnectionAbortedError:
            Exception("redis's connection is wrong")

    def set(self, key, value):
        redis.set(key, value)

if __name__ == '__main__':
    pass