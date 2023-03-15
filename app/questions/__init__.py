from flask import blueprints

bp = Blueprint('questions', __name__)

from app.questions import routes