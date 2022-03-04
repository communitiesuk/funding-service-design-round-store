import json

from flask import Blueprint
from flask import Response as FlaskResponse
from spectree import Response

from . import api
from .models import Round
from .models import RoundList

rounds_bp = Blueprint("rounds_bp", __name__)


@rounds_bp.get("/fund/<fund_id>")
@api.validate(resp=Response(HTTP_200=RoundList), tags=["rounds"])
def get_rounds(fund_id):
    round_item = Round().as_json()
    return FlaskResponse(json.dumps([round_item]), mimetype="application/json")


@rounds_bp.get("/fund/<fund_id>/round/<round_id>")
@api.validate(resp=Response(HTTP_200=Round), tags=["round"])
def get_round(fund_id, round_id):
    return Round().as_json()
