# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CurrentUsage"]


class CurrentUsage(BaseModel):
    requests_this_minute: Optional[int] = None

    requests_today: Optional[int] = None

    reset_time: Optional[datetime] = None
    """When daily limits reset."""

    tokens_this_minute: Optional[int] = None

    tokens_today: Optional[int] = None
