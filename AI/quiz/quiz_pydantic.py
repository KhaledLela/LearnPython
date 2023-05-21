from typing import List

from pydantic import BaseModel, Field, constr, conint, PositiveInt


class Alternative(BaseModel):
    title: str
    correct: conint(ge=0, le=1)


class Question(BaseModel):
    title: str
    question_type_value: constr(regex="^(radio|checkbox)$")
    points: PositiveInt
    alternatives: List[Alternative]


class Quiz(BaseModel):
    title: str = Field(description="quiz title")
    bullets: str = Field(description="quiz summary")
    language_id: int
    question_count: conint(ge=1)
    alternative_count: conint(ge=1)
    questions: List[Question]

    @staticmethod
    def __constrains__(v):
        if len(v.questions) != v.question_count:
            raise ValueError(f"Quiz must have exactly {v.question_count} questions.")
        for question in v.questions:
            if len(question.alternatives) != v.alternative_count:
                raise ValueError(f"Each question must have exactly {v.alternative_count} alternatives.")
        return v
