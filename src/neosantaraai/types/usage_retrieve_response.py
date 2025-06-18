# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .metadata import Metadata
from .current_usage import CurrentUsage

__all__ = ["UsageRetrieveResponse", "Data", "TierInfo", "TierInfoLimits"]


class Data(BaseModel):
    endpoint: Optional[str] = None
    """API endpoint used."""

    model: Optional[str] = None
    """Model used."""

    requests: Optional[int] = None
    """Number of requests."""

    timestamp: Optional[int] = None
    """Usage timestamp."""

    usage: Optional[int] = None
    """Token usage."""


class TierInfoLimits(BaseModel):
    requests_per_day: Optional[int] = None

    requests_per_minute: Optional[int] = None

    tokens_per_day: Optional[int] = None

    tokens_per_minute: Optional[int] = None


class TierInfo(BaseModel):
    expires_at: Optional[datetime] = None
    """Tier expiration date."""

    limits: Optional[TierInfoLimits] = None

    tier: Optional[Literal["free", "basic", "standard", "pro", "enterprise"]] = None


class UsageRetrieveResponse(BaseModel):
    current_usage: Optional[CurrentUsage] = None

    data: Optional[List[Data]] = None

    info_metadata: Optional[Metadata] = None

    object: Optional[str] = None

    tier_info: Optional[TierInfo] = None

    total_requests: Optional[int] = None
    """Total requests made in the period."""

    total_usage: Optional[int] = None
    """Total tokens used in the period."""
