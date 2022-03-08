"""Model for Response Message"""
from pydantic import BaseModel


class ResponseMessage(BaseModel):
    """Pydantic model for response messages"""

    message: str = "Error message"
    status: str = "Status message"
    code: int = "Response code"
