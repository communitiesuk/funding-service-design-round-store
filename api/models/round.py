"""Models for Round"""
from datetime import datetime
from typing import List

from pydantic import BaseModel
from tests.sample_data.rounds import ROUNDS

from .eligibility_criteria import EligibilityCriteria


class Round(BaseModel):
    """Pydantic model for rounds"""

    fund_id: str
    round_title: str
    round_id: str
    eligibility_criteria: EligibilityCriteria = None
    opens: datetime
    deadline: datetime
    application_url: str

    class Config:
        schema_extra = {
            "example": {
                "fund_id": "funding-service-design",
                "round_title": "Spring",
                "round_id": "spring",
                "eligibility_criteria": {"max_project_cost": 1000000},
                "opens": "2022-02-01T00:00:01",
                "deadline": "2022-06-01T00:00:00",
                "application_url": (
                    "https://application-form-service/fund-id-round-id"
                ),
            }
        }

    @staticmethod
    def cached_rounds():
        return ROUNDS

    def as_json(self):
        data = {
            "fund_id": self.fund_id,
            "round_title": self.round_title,
            "round_id": self.round_id,
            "eligibility_criteria": {
                "max_project_cost": self.eligibility_criteria.max_project_cost
            },
            "opens": self.opens.isoformat(),
            "deadline": self.deadline.isoformat(),
            "application_url": self.application_url,
        }
        return data

    @staticmethod
    def from_dict(round_dict: dict):
        return Round(
            fund_id=round_dict.get("fund_id"),
            round_title=round_dict.get("round_title"),
            round_id=round_dict.get("round_id"),
            eligibility_criteria=EligibilityCriteria.from_dict(
                round_dict.get("eligibility_criteria")
            ),
            opens=datetime.fromisoformat(round_dict.get("opens")),
            deadline=datetime.fromisoformat(round_dict.get("deadline")),
            application_url=round_dict.get("application_url"),
        )

    @classmethod
    def list(cls, params: dict, as_json: bool = False):
        fund_id = params.get("fund_id")

        rounds = []
        for fund_round in cls.cached_rounds():
            if fund_round.get("fund_id") == fund_id:
                rounds.append(Round.from_dict(fund_round))

        if as_json:
            return [r.as_json() for r in rounds]

        return rounds

    @classmethod
    def get(cls, params: dict, as_json: bool = False):
        fund_id = params.get("fund_id")
        round_id = params.get("round_id")

        for fund_round in cls.cached_rounds():
            if fund_round.get(
                "fund_id"
            ) == fund_id and round_id == fund_round.get("round_id"):
                found_round = Round.from_dict(fund_round)

                if as_json and found_round:
                    return found_round.as_json()

                return found_round
        return None


class RoundList(BaseModel):
    """Pydantic type model for round lists.
    Currently required for type validation of api requests using Spectree
    """

    __root__: List[Round]
