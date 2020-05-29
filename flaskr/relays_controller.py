import functools

from flask import (
    Blueprint, current_app, jsonify, g, request, url_for
)

bp = Blueprint('relays_controller', __name__, url_prefix='/relays')

RELAY_IDS = list(range(0, 4))

from flaskr.relay_board import get_relay_board

@bp.route('/status')
def status():

  relay_dict = {}

  for relay_id in RELAY_IDS:

    key = __relay_key(relay_id)
    value = __relay_status(relay_id)
    relay_dict[key] = value

  return jsonify(
    relay_dict
  )

@bp.route('/toggle/<relay_id>')
def toggle(relay_id=None):
  if int(relay_id) <= RELAY_IDS[-1]:
    relay_dict = {}

    __toggle_relay(relay_id)

    key = __relay_key(relay_id)
    value = __relay_status(relay_id)
    relay_dict[key] = value

    return jsonify(relay_dict)

  else:
    return 'Relay Unavailable'


def __relay_key(relay_id):
  return 'relay_' + str(relay_id)

def __relay_status(relay_id):
  relays = get_relay_board()
  # import code; code.interact(local=dict(globals(), **locals()))
  relay = relays[int(relay_id)]

  return relay.value

def __toggle_relay(relay_id):
  relays = get_relay_board()
  relay = relays[int(relay_id)]
  return relay.toggle()


