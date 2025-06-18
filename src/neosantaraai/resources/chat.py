# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import chat_create_completion_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.function_param import FunctionParam
from ..types.chat_message_param import ChatMessageParam
from ..types.response_format_param import ResponseFormatParam
from ..types.chat_completions_response import ChatCompletionsResponse

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neosantara-python#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neosantara-python#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)

    def create_completion(
        self,
        *,
        messages: Iterable[ChatMessageParam],
        model: str,
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        functions: Iterable[FunctionParam] | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        presence_penalty: float | NotGiven = NOT_GIVEN,
        response_format: ResponseFormatParam | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: chat_create_completion_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[chat_create_completion_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        web_search: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionsResponse:
        """Create chat completion like OpenAI API.

        Send array of messages (role:
        user/assistant, content: string).

        Args:
          messages: Array of messages (role+content).

          model: Model name (required).

          frequency_penalty: Frequency penalty parameter.

          functions: Available functions for the model to call.

          max_tokens: Maximum number of tokens to generate.

          n: Number of completions to generate.

          presence_penalty: Presence penalty parameter.

          stream: Whether to stream responses.

          temperature: Sampling temperature between 0 and 2.

          tool_choice: Tool choice strategy.

          tools: Available tools for the model to use.

          top_p: Nucleus sampling parameter.

          web_search: Enable web search capabilities.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/chat/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "frequency_penalty": frequency_penalty,
                    "functions": functions,
                    "max_tokens": max_tokens,
                    "n": n,
                    "presence_penalty": presence_penalty,
                    "response_format": response_format,
                    "stream": stream,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_p": top_p,
                    "web_search": web_search,
                },
                chat_create_completion_params.ChatCreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletionsResponse,
        )


class AsyncChatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neosantara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neosantara-python#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)

    async def create_completion(
        self,
        *,
        messages: Iterable[ChatMessageParam],
        model: str,
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        functions: Iterable[FunctionParam] | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        presence_penalty: float | NotGiven = NOT_GIVEN,
        response_format: ResponseFormatParam | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: chat_create_completion_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[chat_create_completion_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        web_search: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionsResponse:
        """Create chat completion like OpenAI API.

        Send array of messages (role:
        user/assistant, content: string).

        Args:
          messages: Array of messages (role+content).

          model: Model name (required).

          frequency_penalty: Frequency penalty parameter.

          functions: Available functions for the model to call.

          max_tokens: Maximum number of tokens to generate.

          n: Number of completions to generate.

          presence_penalty: Presence penalty parameter.

          stream: Whether to stream responses.

          temperature: Sampling temperature between 0 and 2.

          tool_choice: Tool choice strategy.

          tools: Available tools for the model to use.

          top_p: Nucleus sampling parameter.

          web_search: Enable web search capabilities.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/chat/completions",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "frequency_penalty": frequency_penalty,
                    "functions": functions,
                    "max_tokens": max_tokens,
                    "n": n,
                    "presence_penalty": presence_penalty,
                    "response_format": response_format,
                    "stream": stream,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_p": top_p,
                    "web_search": web_search,
                },
                chat_create_completion_params.ChatCreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletionsResponse,
        )


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.create_completion = to_raw_response_wrapper(
            chat.create_completion,
        )


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.create_completion = async_to_raw_response_wrapper(
            chat.create_completion,
        )


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.create_completion = to_streamed_response_wrapper(
            chat.create_completion,
        )


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.create_completion = async_to_streamed_response_wrapper(
            chat.create_completion,
        )
