# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from neosantara import Neosantara, AsyncNeosantara
from tests.utils import assert_matches_type
from neosantara.types import ModerationCreateCheckResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModerations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_check(self, client: Neosantara) -> None:
        moderation = client.moderations.create_check(
            input="This is a test message for moderation.",
        )
        assert_matches_type(ModerationCreateCheckResponse, moderation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_check_with_all_params(self, client: Neosantara) -> None:
        moderation = client.moderations.create_check(
            input="This is a test message for moderation.",
            model="text-moderation-latest",
        )
        assert_matches_type(ModerationCreateCheckResponse, moderation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_check(self, client: Neosantara) -> None:
        response = client.moderations.with_raw_response.create_check(
            input="This is a test message for moderation.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderation = response.parse()
        assert_matches_type(ModerationCreateCheckResponse, moderation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_check(self, client: Neosantara) -> None:
        with client.moderations.with_streaming_response.create_check(
            input="This is a test message for moderation.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            moderation = response.parse()
            assert_matches_type(ModerationCreateCheckResponse, moderation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncModerations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_check(self, async_client: AsyncNeosantara) -> None:
        moderation = await async_client.moderations.create_check(
            input="This is a test message for moderation.",
        )
        assert_matches_type(ModerationCreateCheckResponse, moderation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_check_with_all_params(self, async_client: AsyncNeosantara) -> None:
        moderation = await async_client.moderations.create_check(
            input="This is a test message for moderation.",
            model="text-moderation-latest",
        )
        assert_matches_type(ModerationCreateCheckResponse, moderation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_check(self, async_client: AsyncNeosantara) -> None:
        response = await async_client.moderations.with_raw_response.create_check(
            input="This is a test message for moderation.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderation = await response.parse()
        assert_matches_type(ModerationCreateCheckResponse, moderation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_check(self, async_client: AsyncNeosantara) -> None:
        async with async_client.moderations.with_streaming_response.create_check(
            input="This is a test message for moderation.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            moderation = await response.parse()
            assert_matches_type(ModerationCreateCheckResponse, moderation, path=["response"])

        assert cast(Any, response.is_closed) is True
