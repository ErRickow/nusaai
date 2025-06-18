# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .metadata import Metadata

__all__ = ["ModelListResponse", "Data", "DataPricing"]


class DataPricing(BaseModel):
    currency: Optional[str] = None

    input_tokens: Optional[float] = None
    """Cost per 1K input tokens."""

    output_tokens: Optional[float] = None
    """Cost per 1K output tokens."""


class Data(BaseModel):
    id: Optional[str] = None
    """Model identifier."""

    capabilities: Optional[List[str]] = None
    """Model capabilities."""

    created: Optional[int] = None
    """Model creation timestamp."""

    description: Optional[str] = None
    """Model description."""

    max_tokens: Optional[int] = None
    """Maximum context length."""

    object: Optional[str] = None

    owned_by: Optional[str] = None
    """Organization that owns the model."""

    parent: Optional[str] = None
    """Parent model identifier."""

    permission: Optional[List[builtins.object]] = None

    pricing: Optional[DataPricing] = None

    root: Optional[str] = None
    """Root model identifier."""


class ModelListResponse(BaseModel):
    api_metadata: Optional[Metadata] = FieldInfo(alias="_metadata", default=None)

    data: Optional[List[Data]] = None

    object: Optional[str] = None
