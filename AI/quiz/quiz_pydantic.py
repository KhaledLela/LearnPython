from typing import List
from pydantic import BaseModel, Field, constr, conint, PositiveInt


class Alternative(BaseModel):
    title: str
    alternative: constr(regex="^[A-Z0-9]+$")
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
    tag_names: List[str]
    # media_url: str = Field(description="quiz cover URL")
    questions: List[Question]
