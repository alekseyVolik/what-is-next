from datetime import datetime

from pydantic import (
    BaseModel,
    ConfigDict
)


class CreateGoalSchema(BaseModel):
    """Use to create new Goal"""

    title: str


class GoalSchema(BaseModel):
    """Use to return single Goal representation"""

    id: int
    title: str
    create_at: datetime

    model_config = ConfigDict(from_attributes=True)


class GoalsListSchema(BaseModel):
    """Use to return list Goal representation"""

    goals: list[GoalSchema]



