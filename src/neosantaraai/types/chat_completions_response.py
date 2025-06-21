# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .usage import Usage
from .._models import BaseModel
from .metadata import Metadata
from .chat_message import ChatMessage

__all__ = ["ChatCompletionsResponse", "Choice"]


class Choice(BaseModel):
    finish_reason: Optional[Literal["stop", "length", "function_call", "tool_calls", "content_filter"]] = None
    """Reason for completion finish."""

    index: Optional[int] = None

    message: Optional[ChatMessage] = None


class ChatCompletionsResponse(BaseModel):
    id: Optional[str] = None
    """Completion ID."""

    api_metadata: Optional[Metadata] = FieldInfo(alias="_metadata", default=None)

    choices: Optional[List[Choice]] = None
    """Completion choices."""

    created: Optional[int] = None
    """Creation timestamp."""

    model: Optional[str] = None
    """Model used."""

    object: Optional[str] = None
    """Object type."""

    usage: Optional[Usage] = None
