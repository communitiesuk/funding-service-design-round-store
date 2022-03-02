"""
Contains the tests regarding get requests to the Fund Store API
"""
import json


def test_get_rounds(flask_test_client):
    """
    GIVEN Our Api Fund Store
    WHEN a /rounds/funding-service-design is requested using GET
    THEN check that the get response returns the expected data
    If this test succeeds then our apis is set up and returns
    a list of funds as expected.
    """
    expected_content = [
        {
            "fund_id": "funding-service-design",
            "round_title": "Summer",
            "round_id": "summer",
            "eligibility_criteria": {"maximum_project_cost": 1000000},
            "opens": "2022-06-01T00:00:00",
            "deadline": "2022-08-31T00:00:00",
        },
        {
            "fund_id": "funding-service-design",
            "round_title": "Autumn",
            "round_id": "autumn",
            "eligibility_criteria": {"maximum_project_cost": 10000000},
            "opens": "2022-09-01T00:00:00",
            "deadline": "2022-11-30T00:00:00",
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
    WHEN a /rounds/funding-service-design/summer is requested using GET
    THEN check that the get response returns the expected data
    If this test succeeds then our apis is set up and returns
    detailed infomation about a single fund
    """
    expected_content = {
        "fund_id": "funding-service-design",
        "round_title": "Summer",
        "round_id": "summer",
        "eligibility_criteria": {"maximum_project_cost": 1000000},
        "opens": "2022-06-01T00:00:00",
        "deadline": "2022-08-31T00:00:00",
    }

    response = flask_test_client.get(
        "/fund/funding-service-design/summer", follow_redirects=True
    )
    json_data = json.loads(response.data)
    for key, value in json_data.items():
        assert value == expected_content[key]
