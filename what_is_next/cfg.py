from pathlib import Path
import os

BASE_DIR = Path(os.path.dirname(__file__))

DEFAULT_DB_URI = 'sqlite:///' + str(BASE_DIR / 'app.db')


class FlaskConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', DEFAULT_DB_URI)
