from flask import Flask


def create_app(config=None):
    app = Flask(__name__)

    # Health route
    @app.route('/health')
    def health():
        return {'status': 'I am health'}

    return app
