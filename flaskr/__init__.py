import os

from flask import Flask
import pifacerelayplus
import pifacecommon

relay_board = pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.RELAY)
relays = relay_board.relays

def create_app(test_config=False):

  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(SECRET_KEY='dev')

  if __name__ == "__main__":
      app.run(debug=True)

  from flaskr import relays_controller

  app.register_blueprint(relays_controller.bp)

  return app
