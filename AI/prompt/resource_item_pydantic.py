from typing import List
from pydantic import BaseModel, Field


class ResourceItem(BaseModel):
    title: str = Field(description="The title of the item.")
    language_id: int = Field(description="The language ID associated with the item.")
    tag_names: List[str] = Field(
        description="A list of tags describing the item, which should correspond to Wikipedia article titles.")
    name: str = Field(description="The HTML content of the item, formatted using HTML tags.")
    image_prompt: str = Field(None, description="A prompt for generating a relevant image for the item.")
