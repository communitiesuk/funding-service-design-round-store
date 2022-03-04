"""Contains the set up for our API and a basic DAO
for prototyping.
"""
from flask_restx import fields
from flask_restx import Namespace

api = Namespace(
    "rounds", description="Operations related to funding round information"
)

eligibility_criteria = api.model(
    "Eligibility",
    {
        "maximum_project_cost": fields.Integer(
            description="The maximum amount a project can ask for"
        )
    },
)

fund_round = api.model(
    "Round Data",
    {
        "fund_id": fields.String(
            required=True, description="The ID of the fund"
        ),
        "round_title": fields.String(
            required=True, description="The title of the round"
        ),
        "round_id": fields.String(
            required=True, description="The unique id for this round"
        ),
        "eligibility_criteria": fields.Nested(
            eligibility_criteria,
            required=True,
            desciption="The eligibility criteria of the fund",
        ),
        "opens": fields.DateTime(
            required=True, description="The round opening date"
        ),
        "deadline": fields.DateTime(
            required=True, description="The round closing date"
        ),
        "application_url": fields.String(
            required=True,
            description=(
                "The url for the application form for this funding round"
            ),
        ),
    },
)
