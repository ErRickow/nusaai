# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neosantaraai import Neosantara, AsyncNeosantara
from neosantaraai.types import CompletionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Neosantara) -> None:
        completion = client.completions.create(
            model="nusantara-base",
            prompt="The future of artificial intelligence is",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Neosantara) -> None:
        completion = client.completions.create(
            model="nusantara-base",
            prompt="The future of artificial intelligence is",
            frequency_penalty=-2,
            max_tokens=100,
            n=1,
            presence_penalty=-2,
            response_format={"type": "text"},
            stream=True,
            temperature=0.7,
            top_p=0,
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Neosantara) -> None:
        response = client.completions.with_raw_response.create(
            model="nusantara-base",
            prompt="The future of artificial intelligence is",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Neosantara) -> None:
        with client.completions.with_streaming_response.create(
            model="nusantara-base",
            prompt="The future of artificial intelligence is",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncNeosantara) -> None:
        completion = await async_client.completions.create(
            model="nusantara-base",
            prompt="The future of artificial intelligence is",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncNeosantara) -> None:
        completion = await async_client.completions.create(
            model="nusantara-base",
            prompt="The future of artificial intelligence is",
            frequency_penalty=-2,
            max_tokens=100,
            n=1,
            presence_penalty=-2,
            response_format={"type": "text"},
            stream=True,
            temperature=0.7,
            top_p=0,
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNeosantara) -> None:
        response = await async_client.completions.with_raw_response.create(
            model="nusantara-base",
            prompt="The future of artificial intelligence is",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNeosantara) -> None:
        async with async_client.completions.with_streaming_response.create(
            model="nusantara-base",
            prompt="The future of artificial intelligence is",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True
