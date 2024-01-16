from functools import wraps
from flask import request, make_response, jsonify
import os

def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_secret = os.environ.get("API_SECRET")
        authorization_header = request.headers.get("Authorization")
        if not authorization_header:
            return make_response(jsonify({"message": "Unauthorized"}), 401)
        if authorization_header != api_secret:
            return make_response(jsonify({"message": "Forbidden"}), 403)
        return func(*args, **kwargs)
    return wrapper
