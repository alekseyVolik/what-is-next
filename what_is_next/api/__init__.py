from flask import Blueprint

from what_is_next.api.routes import goals

bp = Blueprint('api', __name__, url_prefix='/api')
bp.register_blueprint(blueprint=goals.bp)
