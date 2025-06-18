# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .response_format_param import ResponseFormatParam

__all__ = ["CompletionCreateParams"]


class CompletionCreateParams(TypedDict, total=False):
    model: Required[str]

    prompt: Required[str]
    """Text prompt for completion."""

    frequency_penalty: float

    max_tokens: int

    n: int

    presence_penalty: float

    response_format: ResponseFormatParam

    stream: bool

    temperature: float

    top_p: float
