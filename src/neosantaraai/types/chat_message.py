# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ChatMessage", "ToolCall", "ToolCallFunction"]


class ToolCallFunction(BaseModel):
    arguments: Optional[str] = None

    name: Optional[str] = None


class ToolCall(BaseModel):
    id: Optional[str] = None

    function: Optional[ToolCallFunction] = None

    type: Optional[Literal["function"]] = None


class ChatMessage(BaseModel):
    content: str
    """Content of the message."""

    role: Literal["system", "user", "assistant"]
    """Role of the message sender."""

    name: Optional[str] = None
    """Optional name of the message sender."""

    tool_calls: Optional[List[ToolCall]] = None
    """Tool calls made by the assistant."""
