import click
from flask import current_app, g
from flask.cli import with_appcontext
import pifacerelayplus

relay_board = pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.RELAY)
relays = relay_board.relays

def get_relay_board():
    if "relay_board" not in g:
        g.relay_board = relays
    return g.relay_board
    """Clear existing data and create new tables."""

@click.command("init-relay_board")

@with_appcontext
def init_relay_board_command():
    """Clear existing data and create new tables."""
    get_relay_board()
    click.echo("Initialized the database.")


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    # app.teardown_appcontext(close_relay_board)
    app.cli.add_command(init_relay_board_command)
