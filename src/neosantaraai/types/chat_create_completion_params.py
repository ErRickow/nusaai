# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .function_param import FunctionParam
from .chat_message_param import ChatMessageParam
from .response_format_param import ResponseFormatParam

__all__ = ["ChatCreateCompletionParams", "ToolChoice", "ToolChoiceToolChoice", "ToolChoiceToolChoiceFunction", "Tool"]


class ChatCreateCompletionParams(TypedDict, total=False):
    messages: Required[Iterable[ChatMessageParam]]
    """Array of messages (role+content)."""

    model: Required[str]
    """Model name (required)."""

    frequency_penalty: float
    """Frequency penalty parameter."""

    functions: Iterable[FunctionParam]
    """Available functions for the model to call."""

    max_tokens: int
    """Maximum number of tokens to generate."""

    n: int
    """Number of completions to generate."""

    presence_penalty: float
    """Presence penalty parameter."""

    response_format: ResponseFormatParam

    stream: bool
    """Whether to stream responses."""

    temperature: float
    """Sampling temperature between 0 and 2."""

    tool_choice: ToolChoice
    """Tool choice strategy."""

    tools: Iterable[Tool]
    """Available tools for the model to use."""

    top_p: float
    """Nucleus sampling parameter."""

    web_search: bool
    """Enable web search capabilities."""


class ToolChoiceToolChoiceFunction(TypedDict, total=False):
    name: str


class ToolChoiceToolChoice(TypedDict, total=False):
    function: ToolChoiceToolChoiceFunction

    type: Literal["function"]


ToolChoice: TypeAlias = Union[str, ToolChoiceToolChoice]


class Tool(TypedDict, total=False):
    type: Required[Literal["function"]]
    """Tool type."""

    function: FunctionParam
