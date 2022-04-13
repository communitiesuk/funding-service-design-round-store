from api.namespace.funds.funds_ns import funds_ns
from api.namespace.rounds.models.rounds import rounds_result
from database.store import ROUNDS
from flask import abort
from flask_restx import Resource


@funds_ns.route("/<fund_id>/rounds", methods=["GET"])
class Rounds(Resource):
    """
    Operations on all rounds for a fund
    """

    @funds_ns.doc("get_rounds")
    @funds_ns.marshal_with(rounds_result, as_list=True, code=200)
    def get(self, fund_id):
        return ROUNDS.get_rounds_of_fund(fund_id), 200


@funds_ns.route("/<fund_id>/rounds/<round_id>", methods=["GET"])
class Round(Resource):
    """
    Operations on a single fund round
    """

    @funds_ns.doc("get_round")
    @funds_ns.marshal_with(rounds_result, code=200)
    def get(self, fund_id, round_id):
        fund_round = ROUNDS.get_round_of_fund(fund_id, round_id)
        if fund_round:
            return fund_round, 200
        else:
            abort(404, "No matching round found")
