import os


class Configuration(object):
    DEBUG = True
    SECRET_KEY = os.urandom(20).hex()
    DATABASE = '/tmp/fl_dz3.db'