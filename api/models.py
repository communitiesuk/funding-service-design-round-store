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


class RoundList(BaseModel):
    __root__: List[Round]
