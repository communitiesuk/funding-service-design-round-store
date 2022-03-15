"""Model for Eligibility Criteria"""
from pydantic import BaseModel


class EligibilityCriteria(BaseModel):
    """Pydantic model for eligibility criteria"""

    max_project_cost: int = None

    @staticmethod
    def from_dict(criteria_dict: dict):
        return EligibilityCriteria(
            max_project_cost=criteria_dict.get("max_project_cost")
        )
