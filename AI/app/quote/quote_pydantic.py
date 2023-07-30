from typing import List
from pydantic import BaseModel, Field


class Quote(BaseModel):
    quote: str = Field(description="The quote body.")
    language_id: int = Field(description="The language ID associated quote.")
    quotee: str = Field(description="A quote author")
    tag_names: List[str] = Field(description="A list of tags describing quote")
    image_prompt: str = Field(
        description="A prompt for generating a relevant image of quote.")
