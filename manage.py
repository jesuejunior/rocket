# encoding: utf-8

from flask.ext.script import Manager

from rocket.settings import app, Metadata

manager = Manager(app)


@manager.command
def create_db():
    """Creates the db tables."""
    print('create_db')
    Metadata.create_all()


@manager.command
def drop_db():
    """Drops the db tables."""
    Metadata.drop_all()


@manager.command
def create_admin():
    """Creates the admin user."""
    # db.session.add(User(email='ad@min.com', password='admin', admin=True))
    # db.session.commit()
    pass


@manager.command
def create_data():
    """Creates sample data."""
    pass


if __name__ == '__main__':
    manager.run()
