# -*- coding: utf-8 -*-
# @author Wu Lihua
# @email maikekechn@gmail.com
import configparser

cf = configparser.ConfigParser()

def import_config():
	return cf.read('./mysql.conf', 'utf-8')

def get_sections_title():
	return cf.sections()




if __name__ == '__main__':
	config_1 = {}
	config_1['mysql'] = '127.0.0.1'

	print(isinstance(config_1, dict))