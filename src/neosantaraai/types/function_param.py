# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FunctionParam"]


class FunctionParam(TypedDict, total=False):
    description: Required[str]
    """Function description."""

    name: Required[str]
    """Function name."""

    parameters: object
    """Function parameters schema."""
