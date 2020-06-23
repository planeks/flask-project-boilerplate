from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


from src.server import db
from src.server import server

migrate = Migrate(server, db)
manager = Manager(server)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
