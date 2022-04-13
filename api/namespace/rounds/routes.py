from api.namespace.rounds.models.rounds import rounds_result
from api.namespace.rounds.rounds_ns import rounds_ns
from database.store import ROUNDS
from flask_restx import reqparse
from flask_restx import Resource


@rounds_ns.route("")
class SearchRounds(Resource):
    """
    GET all relevant rounds with endpoint '?{params}'
    """

    query_params_parser = reqparse.RequestParser()
    query_params_parser.add_argument("fund_id", type=str, help="Round fund_id")
    query_params_parser.add_argument(
        "order_by",
        type=str,
        help="Order results by 'opens' or 'deadline' parameter",
    )
    query_params_parser.add_argument(
        "order_rev",
        type=str,
        help=(
            "Order results by descending (default) or ascending (order_rev=1)"
        ),
    )

    @rounds_ns.doc("get_rounds", parser=query_params_parser)
    @rounds_ns.marshal_with(rounds_result, as_list=True, code=200)
    def get(self):
        args = self.query_params_parser.parse_args()
        response_headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        }
        return ROUNDS.search_rounds(args), 200, response_headers
