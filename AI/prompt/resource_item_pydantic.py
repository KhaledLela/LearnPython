from typing import List

from pydantic import BaseModel, Field


class ResourceItem(BaseModel):
    title: str = Field(description="ITEM title")
    language_id: int = Field(description="ITEM language id")
    tag_names: List[str] = Field(description="ITEM tags that follow Wikipedia article")
    name: str = Field(description="ITEM HTML completion body")
    image_prompt: str = Field(None, description="prompt for generating relevant AI image (optional)")
