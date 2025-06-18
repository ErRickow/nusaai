# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .chat_message_param import ChatMessageParam
from .response_format_param import ResponseFormatParam

__all__ = ["ReasoningCreateParams"]


class ReasoningCreateParams(TypedDict, total=False):
    messages: Required[Iterable[ChatMessageParam]]

    frequency_penalty: float

    max_tokens: int

    model: str

    presence_penalty: float

    response_format: ResponseFormatParam

    stream: bool

    temperature: float

    top_p: float
