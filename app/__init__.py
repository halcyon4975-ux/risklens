from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


db = SQLAlchemy()
migrate = Migrate()


def create_app():

    app = Flask(__name__)

    app.config.from_object("config.Config")

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import blueprints AFTER db exists
    from app.routes.main import main_bp
    from app.routes.assets import assets_bp
    from app.routes.scans import scans_bp


    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(assets_bp)
    app.register_blueprint(scans_bp)

    # Load models for migrations (use importlib to avoid shadowing local `app` variable)
    import importlib
    importlib.import_module("app.models")



    CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "http://127.0.0.1:5173"]}})


    return app