from api.namespace.rounds.rounds_ns import rounds_ns
from flask_restx import fields

eligibility_criteria = rounds_ns.model(
    "eligibility_criteria",
    {
        "max_project_cost": fields.Integer(
            description="Maximum project cost", example="1000000"
        ),
    },
)
