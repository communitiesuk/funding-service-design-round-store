"""
Contains the tests regarding get requests to the Fund Store API
"""
import json


def test_get_rounds(flask_test_client):
    """
    GIVEN Our Api Fund Store
    WHEN /fund/funding-service-design is requested using GET
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
            "opens": "2022-02-01T00:00:01",
            "deadline": "2022-06-01T00:00:00",
            "assessment_deadline": "2022-09-30T00:00:00",
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
            "opens": "2022-06-01T00:00:01",
            "deadline": "2022-08-31T00:00:00",
            "assessment_deadline": "2022-12-30T00:00:00",
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
            "opens": "2022-09-01T00:00:01",
            "deadline": "2022-11-30T00:00:00",
            "assessment_deadline": "2023-03-30T00:00:00",
            "application_url": "".join(
                [
                    "https://funding-service-design-form-runner",
                    ".london.cloudapps.digital/funding-application",
                ]
            ),
        },
    ]
    response = flask_test_client.get(
        "/fund/funding-service-design", follow_redirects=True
    )
    json_data = json.loads(response.data)
    for index, fund in enumerate(json_data):
        for key, value in fund.items():
            assert value == expected_content[index][key]


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
        "opens": "2022-02-01T00:00:01",
        "deadline": "2022-06-01T00:00:00",
        "assessment_deadline": "2022-09-30T00:00:00",
        "application_url": "".join(
            [
                "https://funding-service-design-form-runner",
                ".london.cloudapps.digital/baseline-application-questions",
            ]
        ),
    }

    response = flask_test_client.get(
        "/fund/funding-service-design/round/spring", follow_redirects=True
    )
    json_data = json.loads(response.data)
    for key, value in json_data.items():
        assert value == expected_content[key]
