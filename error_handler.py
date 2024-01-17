import flask

def default_error_handler_azure_functions(e: Exception):
    code = 499

    ret = {
        "Error": "InternalServerError",
        "Description": "Unknown error occurred while processing your request.",
        "Resolution": "Try again later.",
    }

    if isinstance(e,Exception):
        pass
    return flask.jsonify(ret),code