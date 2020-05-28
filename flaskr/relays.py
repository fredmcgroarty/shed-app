import functools
import pifacerelayplus
import pifacecommon

from flask import (
    Blueprint, current_app, jsonify, g, request, url_for
)

bp = Blueprint('relays', __name__, url_prefix='/relays')

RELAY_IDS = list(range(0, 4))


@bp.before_request
def before_request():
  try:
    pfrp = pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.RELAY)
    g.relays = pfrp.relays
  except pifacecommon.spi.SPIInitError:
    g.relays = []


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
  if int(relay_id) and int(relay_id) <= RELAY_IDS[-1] and __relays_available():

    __toggle_relay(relay_id)
    return jsonify({relay_key: __relay_status(relay_id)})

  else:
    return 'Relay Unavailable'


def __relay_key(relay_id):
  return 'relay_' + str(relay_id)


def __relays_available():
  return g.relays != []

def __relay_status(relay_id):
  if __relays_available():
    return g.relays[int(relay_id)].status
  else:
    return 'Relay Unavailable'

def __toggle_relay(relay_id):
  g.relays[relay_id].toggle()


