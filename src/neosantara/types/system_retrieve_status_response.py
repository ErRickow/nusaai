# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .metadata import Metadata
from .current_usage import CurrentUsage

__all__ = ["SystemRetrieveStatusResponse", "System"]


class System(BaseModel):
    last_updated: Optional[datetime] = None

    region: Optional[str] = None
    """Server region."""

    status: Optional[Literal["operational", "degraded", "maintenance", "down"]] = None

    uptime: Optional[float] = None
    """System uptime in seconds."""

    version: Optional[str] = None


class SystemRetrieveStatusResponse(BaseModel):
    api_metadata: Optional[Metadata] = FieldInfo(alias="_metadata", default=None)

    system: Optional[System] = None

    your_tier: Optional[Literal["free", "basic", "standard", "pro", "enterprise"]] = None
    """Your current subscription tier."""

    your_usage: Optional[CurrentUsage] = None
