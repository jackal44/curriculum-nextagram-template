from flask_wtf.csrf import CSRFError
from app import app
from flask_wtf.csrf import CSRFProtect
from flask import render_template, url_for, flash, request
from instagram_web.blueprints.users.views import users_blueprint
from instagram_web.blueprints.sessions.views import sessions_blueprint
from flask_assets import Environment, Bundle
from .util.assets import bundles
from models import user


assets = Environment(app)
assets.register(bundles)

app.register_blueprint(sessions_blueprint, url_prefix="/sessions")
app.register_blueprint(users_blueprint, url_prefix="/users")

csrf = CSRFProtect(app)


@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400


@app.route("/")
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
