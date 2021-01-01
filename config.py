import os
import logging
#from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
#load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    # Keys
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # SQL DB Configuration
    SQL_USERNAME = os.environ.get('MYSQL_USER')
    SQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    SQL_HOST = os.environ.get('MYSQL_HOST') or 'localhost'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:3306/microblog'.format(SQL_USERNAME, SQL_PASSWORD, SQL_HOST)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # E-mail notification settings
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['joe.wr.loesch@gmail.com',
              'joey.loesch@gmail.com']

    # Post Config
    POSTS_PER_PAGE = 5

    # Locale Settings
    LANGUAGES = ['en', 'es']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')

    # Global Logging Level
    LOG_LEVEL = os.environ.get('LOG_LEVEL') or logging.INFO

    ELASTICSEARCH_HOST = os.environ.get('ELASTICSEARCH_HOST') or 'localhost'
    ELASTICSEARCH_URL='http://{}:9200'.format(ELASTICSEARCH_HOST)
