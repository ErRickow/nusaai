# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neosantaraai import Neosantara, AsyncNeosantara
from neosantaraai.types import ChatCompletionsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_completion(self, client: Neosantara) -> None:
        chat = client.chat.create_completion(
            messages=[
                {
                    "content": "What is NusantaraAI?",
                    "role": "user",
                }
            ],
            model="nusantara-base",
        )
        assert_matches_type(ChatCompletionsResponse, chat, path=["response"])

    @parametrize
    def test_method_create_completion_with_all_params(self, client: Neosantara) -> None:
        chat = client.chat.create_completion(
            messages=[
                {
                    "content": "What is NusantaraAI?",
                    "role": "user",
                    "name": "name",
                    "tool_calls": [
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        }
                    ],
                }
            ],
            model="nusantara-base",
            frequency_penalty=-2,
            functions=[
                {
                    "description": "description",
                    "name": "name",
                    "parameters": {},
                }
            ],
            max_tokens=1,
            n=1,
            presence_penalty=-2,
            response_format={"type": "text"},
            stream=True,
            temperature=0,
            tool_choice="string",
            tools=[
                {
                    "type": "function",
                    "function": {
                        "description": "description",
                        "name": "name",
                        "parameters": {},
                    },
                }
            ],
            top_p=0,
            web_search=True,
        )
        assert_matches_type(ChatCompletionsResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_create_completion(self, client: Neosantara) -> None:
        response = client.chat.with_raw_response.create_completion(
            messages=[
                {
                    "content": "What is NusantaraAI?",
                    "role": "user",
                }
            ],
            model="nusantara-base",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatCompletionsResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_create_completion(self, client: Neosantara) -> None:
        with client.chat.with_streaming_response.create_completion(
            messages=[
                {
                    "content": "What is NusantaraAI?",
                    "role": "user",
                }
            ],
            model="nusantara-base",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatCompletionsResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_completion(self, async_client: AsyncNeosantara) -> None:
        chat = await async_client.chat.create_completion(
            messages=[
                {
                    "content": "What is NusantaraAI?",
                    "role": "user",
                }
            ],
            model="nusantara-base",
        )
        assert_matches_type(ChatCompletionsResponse, chat, path=["response"])

    @parametrize
    async def test_method_create_completion_with_all_params(self, async_client: AsyncNeosantara) -> None:
        chat = await async_client.chat.create_completion(
            messages=[
                {
                    "content": "What is NusantaraAI?",
                    "role": "user",
                    "name": "name",
                    "tool_calls": [
                        {
                            "id": "id",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                            "type": "function",
                        }
                    ],
                }
            ],
            model="nusantara-base",
            frequency_penalty=-2,
            functions=[
                {
                    "description": "description",
                    "name": "name",
                    "parameters": {},
                }
            ],
            max_tokens=1,
            n=1,
            presence_penalty=-2,
            response_format={"type": "text"},
            stream=True,
            temperature=0,
            tool_choice="string",
            tools=[
                {
                    "type": "function",
                    "function": {
                        "description": "description",
                        "name": "name",
                        "parameters": {},
                    },
                }
            ],
            top_p=0,
            web_search=True,
        )
        assert_matches_type(ChatCompletionsResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_create_completion(self, async_client: AsyncNeosantara) -> None:
        response = await async_client.chat.with_raw_response.create_completion(
            messages=[
                {
                    "content": "What is NusantaraAI?",
                    "role": "user",
                }
            ],
            model="nusantara-base",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatCompletionsResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_create_completion(self, async_client: AsyncNeosantara) -> None:
        async with async_client.chat.with_streaming_response.create_completion(
            messages=[
                {
                    "content": "What is NusantaraAI?",
                    "role": "user",
                }
            ],
            model="nusantara-base",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatCompletionsResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
