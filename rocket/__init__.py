import os

DB_USER = os.environ.get('DB_USER', 'rocket')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'rocket')
DB_HOST = os.environ.get('DB_HOST', '192.168.99.100')
DB_PORT = os.environ.get('DB_PORT', 5432)
DB_NAME = os.environ.get('DB_NAME', 'rocket')

TEST = os.environ.get('TEST', False)