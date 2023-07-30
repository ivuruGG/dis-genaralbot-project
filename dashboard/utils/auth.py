from flask import Blueprint, redirect, url_for
from flask_dance.contrib.discord import make_discord_blueprint, discord

bp = Blueprint('auth', __name__)

# Discord OAuth configuration
discord_bp = make_discord_blueprint(
    client_id='your-discord-client-id',
    client_secret='your-discord-client-secret',
    scope=["identify", "email"],
)

# Register the blueprint
bp.register_blueprint(discord_bp, url_prefix='/login')


@bp.route('/logout')
def logout():
    discord_bp.session.clear()
    return redirect(url_for('home'))


@discord_bp.route('/discord_authorized')
def discord_logged_in():
    # Retrieve user info from Discord API
    resp = discord.get('/api/users/@me')
    assert resp.ok, resp.text

    # Save the user to the database or session
    user_id = resp.json()['id']
    # ...

    return redirect(url_for('home'))
