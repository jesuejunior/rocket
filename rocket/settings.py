# encoding: utf-8
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import MetaData
from sqlalchemy_utils import database_exists, create_database

SECRET_KEY = 'Fai8/pT1mbXMO62Papz9IdyznrIBuKBzaC2+5uvdxvaX3r2U8tFz/w=='

DB_USER = os.environ.get('DB_USER', 'rocket')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'rocket')
DB_HOST = os.environ.get('DB_HOST', '192.168.99.100')
DB_PORT = os.environ.get('DB_PORT', 5432)
DB_NAME = os.environ.get('DB_NAME', 'rocket')

TEST = os.environ.get('TEST', False)

DEFAULT_DB_TEST_PATH = ''

# Database configuration
if TEST:
    engine = create_engine('postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'
                           .format(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, 'test_rocket'),
                           pool_recycle=3600, echo=False)
else:
    engine = create_engine('postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'
                           .format(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME),
                           pool_recycle=3600, echo=False)

if not database_exists(engine.url):
    create_database(engine.url)

Metadata = MetaData(bind=engine)
Model = declarative_base(metadata=Metadata)
Session = sessionmaker(bind=engine, expire_on_commit=False)