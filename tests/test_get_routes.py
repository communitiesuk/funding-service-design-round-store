"""
Contains the tests regarding get requests to the Fund Store API
"""
from tests.helpers import expected_data_within_get_response


def test_get_rounds(flask_test_client):
    """
    GIVEN Our Api Fund Store
    WHEN /funds/funding-service-design is requested using GET
    THEN check that the get response returns the expected data
    If this test succeeds then our apis is set up and returns
    a list of funds as expected.
    """
    expected_content = [
        {
            "fund_id": "funding-service-design",
            "round_title": "Spring",
            "round_id": "spring",
            "eligibility_criteria": {"max_project_cost": 1200000},
            "opens": "2022-02-01 00:00:01",
            "deadline": "2022-06-01 00:00:00",
            "assessment_deadline": "2022-09-30 00:00:00",
            "application_url": "".join(
                [
                    "https://funding-service-design-form-runner",
                    ".london.cloudapps.digital/baseline-application-questions",
                ]
            ),
        },
        {
            "fund_id": "funding-service-design",
            "round_title": "Summer",
            "round_id": "summer",
            "eligibility_criteria": {"max_project_cost": 1500000},
            "opens": "2022-06-01 00:00:01",
            "deadline": "2022-08-31 00:00:00",
            "assessment_deadline": "2023-03-30 00:00:00",
            "application_url": "".join(
                [
                    "https://funding-service-design-form-runner",
                    ".london.cloudapps.digital/baseline-application-questions",
                ]
            ),
        },
        {
            "fund_id": "funding-service-design",
            "round_title": "Autumn",
            "round_id": "autumn",
            "eligibility_criteria": {"max_project_cost": 10400000},
            "opens": "2022-09-01 00:00:01",
            "deadline": "2022-11-30 00:00:00",
            "assessment_deadline": "2023-03-30 00:00:00",
            "application_url": "".join(
                [
                    "https://funding-service-design-form-runner",
                    ".london.cloudapps.digital/funding-application",
                ]
            ),
        },
    ]

    endpoint = "/funds/funding-service-design"
    endpoint = "/rounds?fund_id=funding-service-design"
    expected_data_within_get_response(
        flask_test_client, endpoint, expected_content
    )


def test_get_round(flask_test_client):
    """
    GIVEN Our Api Fund Store
    WHEN /fund/funding-service-design/spring is requested using GET
    THEN check that the get response returns the expected data
    If this test succeeds then our apis is set up and returns
    detailed information about a single fund
    """
    expected_content = {
        "fund_id": "funding-service-design",
        "round_title": "Spring",
        "round_id": "spring",
        "eligibility_criteria": {"max_project_cost": 1200000},
        "opens": "2022-02-01 00:00:01",
        "deadline": "2022-06-01 00:00:00",
        "assessment_deadline": "2022-09-30 00:00:00",
        "application_url": "".join(
            [
                "https://funding-service-design-form-runner",
                ".london.cloudapps.digital/baseline-application-questions",
            ]
        ),
    }

    endpoint = "/funds/funding-service-design/rounds/spring"
    expected_data_within_get_response(
        flask_test_client, endpoint, expected_content
    )
