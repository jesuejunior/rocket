# encoding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import MetaData
from sqlalchemy_utils import database_exists, create_database

from rocket.settings import TEST, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

DEFAULT_DB_TEST_PATH = ''

# Database configuration
if TEST:
	engine = create_engine('postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'
						   .format(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, 'test_rocket'), pool_recycle=3600, echo=False)
else:
	engine = create_engine('postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'
						   .format(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME), pool_recycle=3600, echo=False)

if not database_exists(engine.url):
	create_database(engine.url)

Metadata = MetaData(bind=engine)
Model = declarative_base(metadata=Metadata)
Session = sessionmaker(bind=engine, expire_on_commit=True)