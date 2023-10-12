from flask import Blueprint

from controllers.TestController import hello

blueprint = Blueprint("blueprint", __name__)

blueprint.route("/", methods=["GET"])(hello)
