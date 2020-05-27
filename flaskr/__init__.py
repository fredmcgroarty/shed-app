from flask import Flask, jsonify
import pifacerelayplus
app = Flask(__name__)

@app.route('/relays/status')
def relay_status():
  return jsonify(
    relay_0_value=1,
    relay_1_value=1,
    relay_2_value=0,
    relay_3_value=0
  )

@app.route('/relays/toggle/<relay_id>')
def toggle_relay(relay_id=None):
  return 'hello' + relay_id


@app.route('/relays/toggle/all')
def toggle_all_relays():
  return 'hello all'
