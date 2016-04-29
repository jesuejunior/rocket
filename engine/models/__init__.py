#!/usr/bin/env python
# encoding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import MetaData

DB_URL = ''
TEST = ''
DEFAULT_DB_TEST_PATH = ''


# Database configuration
if TEST:
    engine = create_engine("sqlite+pysqlite:///{0}".format(DEFAULT_DB_TEST_PATH))
else:
    engine = create_engine(DB_URL, pool_recycle=3600, echo=False)

Metadata = MetaData(bind=engine)
Model = declarative_base(metadata=Metadata)
Session = sessionmaker(bind=engine, expire_on_commit=False)