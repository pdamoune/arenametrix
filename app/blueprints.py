from .main import main as main_blueprint
from .auth import auth as auth_blueprint
from .api import api as api_blueprint
from .models import (
    User, Role, Ticket, Reservation, Spectacle, Representation, Customer)
from app import db


def init_app(app):
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    from app import admin
    if len(admin._views) == 1:  # Secure blueprints for app testing
        admin.add_model_views([
            User,
            Role,
            Ticket,
            Reservation,
            Spectacle,
            Representation,
            Customer
        ], db)
