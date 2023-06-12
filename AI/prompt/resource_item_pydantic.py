from typing import List

from pydantic import BaseModel, Field


class ResourceItem(BaseModel):
    title: str = Field(description="Item title")
    language_id: int = Field(description="Item language id")
    tag_names: List[str] = Field(description="Item tags that follow Wikipedia article")
    name: str = Field(description="Item HTML completion")
