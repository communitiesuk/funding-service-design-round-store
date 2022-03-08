import json

from flask import Response as FlaskResponse


def json_response(response_object: object):
    return FlaskResponse(
        json.dumps(response_object), mimetype="application/json", status=200
    )


def ok_response(message: str):
    return FlaskResponse(
        json.dumps({"message": message, "status": "ok", "code": 200}),
        mimetype="application/json",
        status=200,
    )


def error_response(message: str, code: int = 404):
    return FlaskResponse(
        json.dumps({"message": message, "status": "error", "code": code}),
        mimetype="application/json",
        status=code,
    )
