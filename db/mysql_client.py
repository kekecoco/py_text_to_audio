# -*- coding: utf-8 -*-
# @author Wu Lihua
# @email maikekechn@gmail.com

from peewee import *
from config.mysql_conf import import_mysql_config
import logging

logging.basicConfig(level="INFO")
mysql_cf = import_mysql_config('mysql')

hostname = mysql_cf['hostname']
port = mysql_cf['port']
database = mysql_cf['database']
username = mysql_cf['username']
password = mysql_cf['password']


logging.info("hostname = %s, port = %s, database = %s, username = %s, "
             "password = %s", hostname, port, database, username, password)


mysql_db = MySQLDatabase(database, user=username, password=password, host=hostname, port=int(port))


class BaseModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = mysql_db 


class Account(BaseModel):
    name = CharField()


# account = Account.create(name='Charlie')
account = Account.get(Account.name == 'Charlie')
# print(account.name)

# account.save()
# account.delete()
# print(account.id)

