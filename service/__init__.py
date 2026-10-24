
"""
Package initializer for Customer Accounts Microservice
"""
import sys
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS
from service.common import log_handlers

# Create Flask application
app = Flask(__name__)

# Load configuration
app.config.from_object("config")

# Enable Cross-Origin Resource Sharing (CORS)
CORS(app)

# Enable Security Headers via Flask-Talisman
talisman = Talisman(
    app,
    content_security_policy={
        'default-src': '\'self\'',
        'object-src': '\'none\''
    },
    force_https=False
)

# Set up logging for production
log_handlers.init_app(app)

app.logger.info(70 * "*")
app.logger.info("  A C C O U N T S   S E R V I C E   S T A R T I N G  ".center(70, "*"))
app.logger.info(70 * "*")

try:
    from service import routes, models  # noqa: F401, E402
    from service.common import error_handlers  # noqa: F401, E402
except Exception as error:
    app.logger.critical("%s: Cannot import database package", error)
    sys.exit(4)

app.logger.info("Service initialized successfully.")
