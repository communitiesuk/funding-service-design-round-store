from api.namespace.funds.routes import funds_ns
from api.namespace.rounds.routes import rounds_ns
from flask_restx import Api

api = Api(
    title="Funding Service Design Round Store API",
    version="0.1.0",
    description="Funding Service Design Round Store API",
)

api.add_namespace(rounds_ns)
api.add_namespace(funds_ns)
