# -*- coding: utf-8 -*-
# @author Wu Lihua
# @email maikekechn@gmail.com

import configparser

cf = configparser.ConfigParser()

def importconfig():
	return cf.read('./redis.conf', 'utf-8')

if __name__ == '__main__':
	importconfig()
	print(cf['redis']['hostname'])
