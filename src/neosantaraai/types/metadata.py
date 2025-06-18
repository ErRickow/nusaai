# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Metadata"]


class Metadata(BaseModel):
    creator: Optional[str] = None

    processing_time: Optional[float] = None
    """Processing time in milliseconds."""

    request_id: Optional[str] = None
    """Unique request identifier."""

    status: Optional[bool] = None

    timestamp: Optional[datetime] = None
