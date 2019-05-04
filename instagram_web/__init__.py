from app import app
from flask import render_template, url_for, flash, request
from instagram_web.blueprints.users.views import users_blueprint
from flask_assets import Environment, Bundle
from .util.assets import bundles
from models import user

assets = Environment(app)
assets.register(bundles)

app.register_blueprint(users_blueprint, url_prefix="/users")


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/signUp")
def signup():
    return render_template('users/signup.html')


if __name__ == '__main__':
    app.run(debug=True)
