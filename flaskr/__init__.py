import os

from flask import Flask
from flask_cors import CORS
def create_app(test_config=False):

  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(SECRET_KEY='dev')
  CORS(app)
  from flaskr import relay_board
  relay_board.init_app(app)

  from flaskr import relays_controller

  app.register_blueprint(relays_controller.bp)

  return app
