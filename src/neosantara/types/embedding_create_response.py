# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .metadata import Metadata

__all__ = ["EmbeddingCreateResponse", "Data", "Usage"]


class Data(BaseModel):
    embedding: Optional[List[float]] = None
    """Vector embedding values."""

    index: Optional[int] = None
    """Index of the input text."""

    object: Optional[str] = None


class Usage(BaseModel):
    prompt_tokens: Optional[int] = None

    total_tokens: Optional[int] = None


class EmbeddingCreateResponse(BaseModel):
    api_metadata: Optional[Metadata] = FieldInfo(alias="_metadata", default=None)

    data: Optional[List[Data]] = None

    model: Optional[str] = None

    object: Optional[str] = None

    usage: Optional[Usage] = None
