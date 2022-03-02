"""
Imports the API from fund_app.py and creates the routes
in it.
"""
from apis.dao import FundingRounds
from apis.dummy_data import ROUND_DATA
from apis.models import api
from apis.models import fund_round
from flask_restx import Resource

ROUNDS = FundingRounds()
ROUNDS.load_dummy(ROUND_DATA)


@api.route("/<fund_id>")
class RoundList(Resource):
    @api.doc("list_rounds")
    @api.marshal_list_with(fund_round)
    def get(self, fund_id: str):
        """List all rounds for a fund"""
        return ROUNDS.get_all(fund_id)


@api.route("/<fund_id>/<round_id>")
@api.param("fund_id", "The id of the fund")
@api.param("round_id", "The id of the round")
@api.response(404, "Round not found")
class Round(Resource):
    @api.doc("get_round")
    @api.marshal_with(fund_round)
    def get(self, fund_id, round_id):
        """Fetch a round given a fund_id and a round_id"""
        return ROUNDS.get(fund_id, round_id)
