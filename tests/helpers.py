import json

from deepdiff import DeepDiff


def expected_data_within_get_response(
    test_client, endpoint: str, expected_data
):
    """
    Given a endpoint and expected content,
    check to see if response contains expected data

    Args:
        test_client: A flask test client
        endpoint (str): The GET request endpoint
        expected_data: The content we expect to find

    """
    response = test_client.get(endpoint, follow_redirects=True)
    response_data = json.loads(response.data)

    diff = DeepDiff(expected_data, response_data)

    error_message = "Expected data does not match response: " + str(diff)
    assert diff == {}, error_message


def post_data(test_client, endpoint: str, data: dict, expected_data: dict):
    """Given an endpoint and data, check to see if response contains expected data

    Args:
        test_client: A flask test client
        endpoint (str): The POST request endpoint
        data (dict): The content to post to the endpoint provided
        expected_data (dict): The expected response data
    """

    response = test_client.post(
        endpoint,
        data=json.dumps(data),
        content_type="application/json",
        follow_redirects=True,
    )
    response_data = json.loads(response.data)

    diff = DeepDiff(expected_data, response_data)

    error_message = "Expected data does not match response: " + str(diff)
    assert diff == {}, error_message


def count_fund_rounds(test_client, fund_id: str, expected_rounds_count: int):
    """
    Given a fund_id, check the number of rounds

    Args:
        test_client: A flask test client
        fund_id (str): The id of the fund to count applications
        expected_rounds_count (int):
        The expected number of rounds for the fund

    """
    fund_rounds_endpoint = f"/rounds?fund_id={fund_id}"
    response = test_client.get(fund_rounds_endpoint, follow_redirects=True)
    response_data = json.loads(response.data)
    error_message = (
        "Response from "
        + fund_rounds_endpoint
        + " found "
        + str(len(response_data))
        + " items, but expected "
        + str(expected_rounds_count)
    )
    assert len(response_data) == expected_rounds_count, error_message
