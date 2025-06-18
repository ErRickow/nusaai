# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from neosantara import Neosantara, AsyncNeosantara
from tests.utils import assert_matches_type
from neosantara.types import SystemRetrieveStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSystem:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_status(self, client: Neosantara) -> None:
        system = client.system.retrieve_status()
        assert_matches_type(SystemRetrieveStatusResponse, system, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_status(self, client: Neosantara) -> None:
        response = client.system.with_raw_response.retrieve_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        system = response.parse()
        assert_matches_type(SystemRetrieveStatusResponse, system, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_status(self, client: Neosantara) -> None:
        with client.system.with_streaming_response.retrieve_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            system = response.parse()
            assert_matches_type(SystemRetrieveStatusResponse, system, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSystem:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncNeosantara) -> None:
        system = await async_client.system.retrieve_status()
        assert_matches_type(SystemRetrieveStatusResponse, system, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncNeosantara) -> None:
        response = await async_client.system.with_raw_response.retrieve_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        system = await response.parse()
        assert_matches_type(SystemRetrieveStatusResponse, system, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncNeosantara) -> None:
        async with async_client.system.with_streaming_response.retrieve_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            system = await response.parse()
            assert_matches_type(SystemRetrieveStatusResponse, system, path=["response"])

        assert cast(Any, response.is_closed) is True
