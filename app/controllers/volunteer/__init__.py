from flask import Blueprint

# Blueprint Configuration
volunteer_bp = Blueprint(
    'volunteer', __name__,
    template_folder='templates',
    static_folder='static'
)

from app.controllers.volunteer import routes
