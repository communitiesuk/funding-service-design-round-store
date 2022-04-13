from dateutil import parser as date_parser

initial_round_store_state = {
    "funding-service-design:spring": {
        "id": "funding-service-design:spring",
        "fund_id": "funding-service-design",
        "round_title": "Spring",
        "round_id": "spring",
        "eligibility_criteria": {"max_project_cost": 1200000},
        "opens": date_parser.parse("2022-02-01 00:00:01"),
        "deadline": date_parser.parse("2022-06-01 00:00:00"),
        "assessment_deadline": date_parser.parse("2022-09-30 00:00:00"),
        "application_url": "".join(
            [
                "https://funding-service-design-form-runner",
                ".london.cloudapps.digital/baseline-application-questions",
            ]
        ),
    },
    "funding-service-design:summer": {
        "id": "funding-service-design:summer",
        "fund_id": "funding-service-design",
        "round_title": "Summer",
        "round_id": "summer",
        "eligibility_criteria": {"max_project_cost": 1500000},
        "opens": date_parser.parse("2022-06-01 00:00:01"),
        "deadline": date_parser.parse("2022-08-31 00:00:00"),
        "assessment_deadline": date_parser.parse("2023-03-30 00:00:00"),
        "application_url": "".join(
            [
                "https://funding-service-design-form-runner",
                ".london.cloudapps.digital/baseline-application-questions",
            ]
        ),
    },
    "funding-service-design:autumn": {
        "id": "funding-service-design:autumn",
        "fund_id": "funding-service-design",
        "round_title": "Autumn",
        "round_id": "autumn",
        "eligibility_criteria": {"max_project_cost": 10400000},
        "opens": date_parser.parse("2022-09-01 00:00:01"),
        "deadline": date_parser.parse("2022-11-30 00:00:00"),
        "assessment_deadline": date_parser.parse("2023-03-30 00:00:00"),
        "application_url": "".join(
            [
                "https://funding-service-design-form-runner",
                ".london.cloudapps.digital/funding-application",
            ]
        ),
    },
}
