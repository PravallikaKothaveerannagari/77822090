from app import create_app
from error_handler import default_error_handler_azure_functions
from flask import jsonify

app = create_app()


@app.errorhandler(Exception)
def handle_error(e):
    return default_error_handler_azure_functions(e)


