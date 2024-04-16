from flask import Blueprint, request, jsonify

# import adapters
from src.main.adapters.request_adapter import request_adapter

# import compose
from src.main.composes.user_finder_compose import user_finder_compose
from src.main.composes.user_register_compose import user_register_compose

user_route_bp = Blueprint("use_routes", __name__)


@user_route_bp.route("/user/find", methods=["GET"])
def find_user():
    http_response = request_adapter(request, user_finder_compose())
    return jsonify(http_response.body), http_response.status_code


@user_route_bp.route("/user", methods=["POST"])
def register_user():
    http_response = request_adapter(request, user_register_compose())
    return jsonify(http_response.body), http_response.status_code
