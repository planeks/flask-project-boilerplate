import os
from dotenv import load_dotenv

load_dotenv()


POSTGRES = {
    'user': os.getenv('POSTGRES_USER', 'postgres'),
    'pw': os.getenv('POSTGRES_PW', ''),
    'host': os.getenv('POSTGRES_HOST', 'http://127.0.0.1'),
    'port': os.getenv('POSTGRES_PORT', '5432'),
    'db': os.getenv('POSTGRES_DB', 'postgres'),
}


class Config(object):
    SQLALCHEMY_DATABASE_URI = f'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    SITE_URL = os.getenv('SITE_URL', "localhost:5000")
