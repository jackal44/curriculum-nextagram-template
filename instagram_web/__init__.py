from flask_wtf.csrf import CSRFError
from app import app
from flask_wtf.csrf import CSRFProtect
from flask import render_template, url_for, flash, request
from instagram_web.blueprints.users.views import users_blueprint
from instagram_web.blueprints.sessions.views import sessions_blueprint
from instagram_web.blueprints.images.views import images_blueprint
from flask_assets import Environment, Bundle
from .util.assets import bundles
from models.user import User
from app import login_manager
from werkzeug import secure_filename


assets = Environment(app)
assets.register(bundles)


app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(images_blueprint, url_prefix="/images")
app.register_blueprint(sessions_blueprint, url_prefix="/sessions")

csrf = CSRFProtect(app)


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)


@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html')


@app.route("/")
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
