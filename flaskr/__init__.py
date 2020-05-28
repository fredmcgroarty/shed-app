# from flask import Flask, jsonify
# app = Flask(__name__)

import os

from flask import Flask

def create_app(test_config=False):
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(SECRET_KEY='dev')

  if __name__ == "__main__":
      app.run(debug=True)

  from flaskr import relays

  app.register_blueprint(relays.bp)

  return app
