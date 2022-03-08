from flask import Blueprint
from flask import redirect
from spectree import Response
from spectree import Tag

from . import api
from .models.response_message import ResponseMessage
from .models.round import Round
from .models.round import RoundList
from .responses import error_response
from .responses import json_response

rounds_bp = Blueprint("rounds_bp", __name__)

# Label tags for api documentation
round_tag = Tag(
    name="round", description="Operations related to individual rounds"
)
rounds_tag = Tag(
    name="rounds", description="Operations related to all rounds for a fund"
)


# Default Routes
@rounds_bp.get("/")
def docs():
    """Redirect homepage to swagger docs
    (Redoc also available at /api/redoc)
    """
    return redirect("/apidoc/swagger")


# API Routes
@rounds_bp.get("/fund/<fund_id>")
@api.validate(
    resp=Response(HTTP_200=RoundList, HTTP_404=ResponseMessage),
    tags=[rounds_tag],
)
def list_rounds(fund_id):
    """Lists all rounds for a given fund.
    Returns: List of Rounds as json 200
    OR error_message 404"""
    rounds = Round.list(params={"fund_id": fund_id}, as_json=True)
    if rounds:
        return json_response(rounds)
    else:
        return error_response("No rounds found")


@rounds_bp.get("/fund/<fund_id>/round/<round_id>")
@api.validate(
    resp=Response(HTTP_200=Round, HTTP_404=ResponseMessage), tags=[round_tag]
)
def get_round(fund_id, round_id):
    """Gets full details for a funding round.
    Returns: Round as json 200
    OR error_message 404"""
    found_round = Round.get(
        params={"fund_id": fund_id, "round_id": round_id}, as_json=True
    )
    if found_round:
        return found_round
    else:
        return error_response("Round not found")
