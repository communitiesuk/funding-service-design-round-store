from datetime import datetime
from typing import List

from pydantic import BaseModel


class Query(BaseModel):
    text: str = "default query strings"


class EligibilityCriteria(BaseModel):
    maximum_project_cost: int = 1000000


class Round(BaseModel):
    fund_id: str = "funding-service-design"
    round_title: str = "Spring"
    round_id: str = "spring"
    eligibility_criteria: EligibilityCriteria = EligibilityCriteria()
    opens: datetime = datetime.fromisoformat("2022-02-01T00:00:01")
    deadline: datetime = datetime.fromisoformat("2022-02-01T00:00:01")

    class Config:
        schema_extra = {
            "example": {
                "fund_id": "funding-service-design",
                "round_title": "Spring",
                "round_id": "spring",
                "eligibility_criteria": {"maximum_project_cost": 1000000},
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
                "maximum_project_cost": self.eligibility_criteria.maximum_project_cost  # noqa
            },
            "opens": self.opens.isoformat(),
            "deadline": self.deadline.isoformat(),
        }
        return data


class RoundList(BaseModel):
    __root__: List[Round]
