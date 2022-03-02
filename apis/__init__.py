from apis.routes import api as fund_api
from flask_restx import Api

api = Api(
    title="Round Store API",
    version="0.1",
    description=(
        "An api for requesting information about funding rounds from the"
        " funding round store"
    ),
)

api.add_namespace(fund_api, path="/fund")
