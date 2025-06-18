# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import reasoning_create_params
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
from ..types.chat_message_param import ChatMessageParam
from ..types.response_format_param import ResponseFormatParam
from ..types.chat_completions_response import ChatCompletionsResponse

__all__ = ["ReasoningResource", "AsyncReasoningResource"]


class ReasoningResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReasoningResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neosantara-python#accessing-raw-response-data-eg-headers
        """
        return ReasoningResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReasoningResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neosantara-python#with_streaming_response
        """
        return ReasoningResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        messages: Iterable[ChatMessageParam],
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        presence_penalty: float | NotGiven = NOT_GIVEN,
        response_format: ResponseFormatParam | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionsResponse:
        """
        Advanced reasoning capabilities with enhanced context understanding.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/reasoning",
            body=maybe_transform(
                {
                    "messages": messages,
                    "frequency_penalty": frequency_penalty,
                    "max_tokens": max_tokens,
                    "model": model,
                    "presence_penalty": presence_penalty,
                    "response_format": response_format,
                    "stream": stream,
                    "temperature": temperature,
                    "top_p": top_p,
                },
                reasoning_create_params.ReasoningCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletionsResponse,
        )


class AsyncReasoningResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReasoningResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neosantara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReasoningResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReasoningResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neosantara-python#with_streaming_response
        """
        return AsyncReasoningResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        messages: Iterable[ChatMessageParam],
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        presence_penalty: float | NotGiven = NOT_GIVEN,
        response_format: ResponseFormatParam | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletionsResponse:
        """
        Advanced reasoning capabilities with enhanced context understanding.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/reasoning",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "frequency_penalty": frequency_penalty,
                    "max_tokens": max_tokens,
                    "model": model,
                    "presence_penalty": presence_penalty,
                    "response_format": response_format,
                    "stream": stream,
                    "temperature": temperature,
                    "top_p": top_p,
                },
                reasoning_create_params.ReasoningCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletionsResponse,
        )


class ReasoningResourceWithRawResponse:
    def __init__(self, reasoning: ReasoningResource) -> None:
        self._reasoning = reasoning

        self.create = to_raw_response_wrapper(
            reasoning.create,
        )


class AsyncReasoningResourceWithRawResponse:
    def __init__(self, reasoning: AsyncReasoningResource) -> None:
        self._reasoning = reasoning

        self.create = async_to_raw_response_wrapper(
            reasoning.create,
        )


class ReasoningResourceWithStreamingResponse:
    def __init__(self, reasoning: ReasoningResource) -> None:
        self._reasoning = reasoning

        self.create = to_streamed_response_wrapper(
            reasoning.create,
        )


class AsyncReasoningResourceWithStreamingResponse:
    def __init__(self, reasoning: AsyncReasoningResource) -> None:
        self._reasoning = reasoning

        self.create = async_to_streamed_response_wrapper(
            reasoning.create,
        )
