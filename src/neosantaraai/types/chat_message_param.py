# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatMessageParam", "ToolCall", "ToolCallFunction"]


class ToolCallFunction(TypedDict, total=False):
    arguments: str

    name: str


class ToolCall(TypedDict, total=False):
    id: str

    function: ToolCallFunction

    type: Literal["function"]


class ChatMessageParam(TypedDict, total=False):
    content: Required[str]
    """Content of the message."""

    role: Required[Literal["system", "user", "assistant"]]
    """Role of the message sender."""

    name: str
    """Optional name of the message sender."""

    tool_calls: Iterable[ToolCall]
    """Tool calls made by the assistant."""
