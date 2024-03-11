from what_is_next import cfg

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate_manager = Migrate()


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(cfg.FlaskConfig)

    # Registry plugins
    db.init_app(app)
    migrate_manager.init_app(app, db)

    # Registry Blueprints
    from what_is_next.api import bp as api_bp

    app.register_blueprint(blueprint=api_bp)

    # Health route
    @app.route('/health')
    def health():
        return {'status': 'I am health'}

    return app
