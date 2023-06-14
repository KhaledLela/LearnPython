from typing import List
from pydantic import BaseModel, Field


class ResourceItem(BaseModel):
    title: str = Field(description="Title of the item")
    language_id: int = Field(description="Language ID of the item")
    tag_names: List[str] = Field(description="Tags describing the item (follow Wikipedia article titles)")
    name: str = Field(description="HTML completion body of the item")
    image_prompt: str = Field(
        None,
        description="Prompt for generating a relevant image (concise summary of the 'name' field)"
    )
