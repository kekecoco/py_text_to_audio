# -*- coding: utf-8 -*-
# @author Wu Lihua
# @email maikekechn@gmail.com
import configparser

# 应用配置
application_path = '/Users/deepin/py_text_to_audio'
config_path = application_path + '/config'
mysql_config_file = config_path + '/mysql.conf'
redis_config_file = config_path + '/redis.conf'
log_path = application_path + '/runtime/log'
error_log_path = application_path + '/runtime/error'


# 配置文件初始化
def configInit(config_file_name):
    config_file = config_path + '/' + config_file_name
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file, 'utf-8')
    return config_parser

# 返回可用的section列表
def get_sections_title(config_file_name):
    config_parser = configInit(config_file_name)
    return config_parser.sections()

# 获取当前所有section
def get_sections(config_file_name, section):
    if not config_file_name:
        return False
    if not section:
        return False

    config_parser = configInit(config_file_name)
    if not config_parser.has_section(section):
        return False

    return config_parser.options(section)

# 返回指定section中的某个值
def get_option(config_file_name, section, option):
    if not config_file_name:
        return False
    if not section:
        return False
    if not option:
        return False

    config_parser = configInit(config_file_name)
    if not config_parser.has_section(section):
        return False
    if not config_parser.has_option(section, option):
        return False

    return config_parser.get(section, option)

if __name__ == '__main__':
    pass