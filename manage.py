# encoding: utf-8

from flask.ext.script import Manager

from rocket.settings import app

manager = Manager(app)


@manager.command
def create_db():
    """Creates the db tables."""
    # db.create_all()
    print('create_db')
    return True

@manager.command
def drop_db():
    """Drops the db tables."""
    # db.drop_all()
    pass


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
