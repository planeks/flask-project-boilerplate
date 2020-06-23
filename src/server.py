from flask import Flask
from flask_cors import CORS

from src import config as configuration
from flask_sqlalchemy import SQLAlchemy


server = Flask(__name__)

server.config.from_object(configuration.Config)

db = SQLAlchemy()

db.init_app(server)
db.app = server

CORS(
    server,
    resources={r"/*": {"origins": "*"}},
    headers=['Content-Type', 'X-Requested-With', 'Authorization']
)


from src.route.user import user_blueprint
server.register_blueprint(user_blueprint)


if __name__ == '__main__':
    server.run(debug=True)
