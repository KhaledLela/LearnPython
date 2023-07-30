from typing import List
from pydantic import BaseModel, Field


class ResourceItem(BaseModel):
    title: str = Field(description="The title of the item.")
    language_id: int = Field(
        description="The language ID associated with the item.")
    description: str = Field(description="A concise summary in bullets")
    text: str = Field(description="The content text of the item, formatted in HTML.")
    tag_names: List[str] = Field(
        description="A list of tags describing the item, which should correspond to Wikipedia article titles.")
    image_prompt: str = Field(
        description="A prompt for generating a relevant image for the item.")
