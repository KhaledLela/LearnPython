from typing import List

from pydantic import BaseModel, Field, constr, conint
from pydantic.types import PositiveInt


class Alternative(BaseModel):
    title: str
    correct: conint(ge=0, le=1)
    points: conint(ge=0)


class Question(BaseModel):
    title: str
    question_type_value: constr(regex="^(radio|checkbox)$")
    points: PositiveInt
    alternatives: List[Alternative]


class Quiz(BaseModel):
    title: str = Field(description="quiz title")
    bullets: str = Field(description="quiz summary")
    language_id: int
    questions: List[Question]
