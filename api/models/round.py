"""Models for Round"""
from __future__ import annotations

from datetime import datetime
from typing import List

from api.models.eligibility_criteria import EligibilityCriteria
from pydantic import BaseModel
from tests.sample_data.rounds import ROUNDS


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

    @classmethod
    def cached_rounds(cls):
        """
        Placeholder for persistent data store for use in search
        (currently just a list of round jsons)

        Returns: a cached list of round data as json

        """
        return ROUNDS

    def as_json(self):
        """
        Renders a Round instance as a valid json

        Returns: json representation of a Round

        """
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
        """
        Creates a Round from a json dict

        Args:
            round_dict: a json representation of a round

        Returns: Round

        """
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
    def list(cls, params: dict, as_json: bool = False) -> List | None:
        """
        Return a filtered list of rounds from cached_rounds()

        Args:
            params: dict of filters
            as_json: bool to return as a list of jsons objects

        Returns: List of Rounds, List of jsons, or None

        """
        fund_id = params.get("fund_id")

        rounds = []
        for fund_round in cls.cached_rounds():
            if fund_round.get("fund_id") == fund_id:
                rounds.append(Round.from_dict(fund_round))

        if as_json:
            return [r.as_json() for r in rounds]

        return rounds

    @classmethod
    def get(
        cls, fund_id: str, round_id: str, as_json: bool = False
    ) -> Round | dict | None:
        """
        Get a single Round from cached_rounds()

        Args:
            fund_id: The id key of the fund
            round_id: The id key of the round
            as_json: bool to return as a list of jsons objects

        Returns: Round, json representation of a round, or None

        """
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
