from api.namespace.rounds.models.eligibility_criteria import (
    eligibility_criteria,
)
from api.namespace.rounds.rounds_ns import rounds_ns
from flask_restx import fields

rounds_result = rounds_ns.model(
    "rounds_result",
    {
        "round_id": fields.String(
            description="The id of the round", example="spring"
        ),
        "round_title": fields.String(
            description="The title of the round", example="NOT_STARTED"
        ),
        "fund_id": fields.String(
            description="The id of the fund", example="funding-service-design"
        ),
        "eligibility_criteria": fields.Nested(
            eligibility_criteria,
            description="Applicant eligibility criteria",
        ),
        "opens": fields.String(
            description="The datetime the round opens",
            example="2022-12-25 00:00:00",
        ),
        "deadline": fields.String(
            description="The datetime deadline for round submissions",
            example="2022-12-25 00:00:00",
        ),
        "assessment_deadline": fields.String(
            description="The assessment deadline for this round",
            example="2022-12-25 00:00:00",
        ),
        "application_url": fields.String(
            description="The url for the online application form",
            example="https://application-form-service/fund-id-round-id",
        ),
    },
)
