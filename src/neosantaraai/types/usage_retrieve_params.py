# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UsageRetrieveParams"]


class UsageRetrieveParams(TypedDict, total=False):
    end_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """End date for usage statistics (YYYY-MM-DD)"""

    start_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Start date for usage statistics (YYYY-MM-DD)"""
