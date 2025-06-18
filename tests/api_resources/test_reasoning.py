# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neosantaraai import Neosantara, AsyncNeosantara
from neosantaraai.types import ChatCompletionsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReasoning:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Neosantara) -> None:
        reasoning = client.reasoning.create(
            messages=[
                {
                    "content": "Solve this step by step: If a train travels 120 km in 2 hours, and then 180 km in 3 hours, what is the average speed for the entire journey?",
                    "role": "user",
                }
            ],
        )
        assert_matches_type(ChatCompletionsResponse, reasoning, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Neosantara) -> None:
        reasoning = client.reasoning.create(
            messages=[
                {
                    "content": "Solve this step by step: If a train travels 120 km in 2 hours, and then 180 km in 3 hours, what is the average speed for the entire journey?",
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
            frequency_penalty=-2,
            max_tokens=1500,
            model="nusantara-base",
            presence_penalty=-2,
            response_format={"type": "text"},
            stream=True,
            temperature=0.3,
            top_p=0,
        )
        assert_matches_type(ChatCompletionsResponse, reasoning, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Neosantara) -> None:
        response = client.reasoning.with_raw_response.create(
            messages=[
                {
                    "content": "Solve this step by step: If a train travels 120 km in 2 hours, and then 180 km in 3 hours, what is the average speed for the entire journey?",
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reasoning = response.parse()
        assert_matches_type(ChatCompletionsResponse, reasoning, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Neosantara) -> None:
        with client.reasoning.with_streaming_response.create(
            messages=[
                {
                    "content": "Solve this step by step: If a train travels 120 km in 2 hours, and then 180 km in 3 hours, what is the average speed for the entire journey?",
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reasoning = response.parse()
            assert_matches_type(ChatCompletionsResponse, reasoning, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReasoning:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncNeosantara) -> None:
        reasoning = await async_client.reasoning.create(
            messages=[
                {
                    "content": "Solve this step by step: If a train travels 120 km in 2 hours, and then 180 km in 3 hours, what is the average speed for the entire journey?",
                    "role": "user",
                }
            ],
        )
        assert_matches_type(ChatCompletionsResponse, reasoning, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncNeosantara) -> None:
        reasoning = await async_client.reasoning.create(
            messages=[
                {
                    "content": "Solve this step by step: If a train travels 120 km in 2 hours, and then 180 km in 3 hours, what is the average speed for the entire journey?",
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
            frequency_penalty=-2,
            max_tokens=1500,
            model="nusantara-base",
            presence_penalty=-2,
            response_format={"type": "text"},
            stream=True,
            temperature=0.3,
            top_p=0,
        )
        assert_matches_type(ChatCompletionsResponse, reasoning, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNeosantara) -> None:
        response = await async_client.reasoning.with_raw_response.create(
            messages=[
                {
                    "content": "Solve this step by step: If a train travels 120 km in 2 hours, and then 180 km in 3 hours, what is the average speed for the entire journey?",
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reasoning = await response.parse()
        assert_matches_type(ChatCompletionsResponse, reasoning, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNeosantara) -> None:
        async with async_client.reasoning.with_streaming_response.create(
            messages=[
                {
                    "content": "Solve this step by step: If a train travels 120 km in 2 hours, and then 180 km in 3 hours, what is the average speed for the entire journey?",
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reasoning = await response.parse()
            assert_matches_type(ChatCompletionsResponse, reasoning, path=["response"])

        assert cast(Any, response.is_closed) is True
