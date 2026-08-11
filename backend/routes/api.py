from flask import Blueprint

api = Blueprint("api", __name__)


@api.route("/health")
def health():
    return {
        "servicio": "Germania API",
        "estado": "activo"
    }
