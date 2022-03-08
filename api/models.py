from datetime import datetime
from typing import List

from pydantic import BaseModel


class Query(BaseModel):
    text: str = "default query strings"


class ResponseMessage(BaseModel):
    message: str = "Error message"
    status: str = "Status message"
    code: int = "Response code"


class EligibilityCriteria(BaseModel):
    max_project_cost: int = None

    @staticmethod
    def from_dict(criteria_dict: dict):
        return EligibilityCriteria(
            max_project_cost=criteria_dict.get("max_project_cost")
        )


class Round(BaseModel):
    fund_id: str = "funding-service-design"
    round_title: str = "Spring"
    round_id: str = "spring"
    eligibility_criteria: EligibilityCriteria = None
    opens: datetime = datetime.fromisoformat("2022-02-01T00:00:01")
    deadline: datetime = datetime.fromisoformat("2022-02-01T00:00:01")

    class Config:
        schema_extra = {
            "example": {
                "fund_id": "funding-service-design",
                "round_title": "Spring",
                "round_id": "spring",
                "eligibility_criteria": {"max_project_cost": 1000000},
                "opens": "2022-02-01T00:00:01",
                "deadline": "2022-06-01T00:00:00",
            }
        }

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
        )


class RoundList(BaseModel):
    __root__: List[Round]
