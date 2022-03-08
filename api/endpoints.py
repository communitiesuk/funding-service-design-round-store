from flask import Blueprint
from flask import redirect
from spectree import Response
from spectree import Tag

from . import api
from .data import select_json_round
from .data import select_json_rounds
from .models import ResponseMessage
from .models import Round
from .models import RoundList
from .responses import error_response
from .responses import json_response

rounds_bp = Blueprint("rounds_bp", __name__)

round_tag = Tag(
    name="round", description="Operations related to individual rounds"
)
rounds_tag = Tag(
    name="rounds", description="Operations related to all rounds for a fund"
)


@rounds_bp.get("/")
def docs():
    return redirect("/apidoc/swagger")


@rounds_bp.get("/fund/<fund_id>")
@api.validate(
    resp=Response(HTTP_200=RoundList, HTTP_404=ResponseMessage),
    tags=[rounds_tag],
)
def get_rounds(fund_id):
    """Lists all rounds for a given fund"""
    rounds = select_json_rounds(fund_id)
    if rounds:
        return json_response(rounds)
    else:
        return error_response("No rounds found")


@rounds_bp.get("/fund/<fund_id>/round/<round_id>")
@api.validate(
    resp=Response(HTTP_200=Round, HTTP_404=ResponseMessage), tags=[round_tag]
)
def get_round(fund_id, round_id):
    """Gets full details for a funding round"""
    found_round = select_json_round(fund_id, round_id)
    if found_round:
        return found_round
    else:
        return error_response("Round not found")
