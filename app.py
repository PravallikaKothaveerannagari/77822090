import flask
from flask_cors import CORS
from error_handler import default_error_handler_azure_functions
import logging


def create_app():
    app = flask.Flask(__name__)
    CORS(app)
    app.config.from_prefixed_env()

    if "TESTING" in app.config or not app.config["TESTING"]:
        logging.info("Connected")

    app.register_error_handler(Exception, default_error_handler_azure_functions)

    return app

app = create_app()
if __name__== "__main__":
 app.run(debug=True, host="0.0.0.0")
