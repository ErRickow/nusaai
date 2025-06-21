# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["EmbeddingCreateParams"]


class EmbeddingCreateParams(TypedDict, total=False):
    input: Required[Union[str, List[str]]]
    """Input text(s) to generate embeddings for."""

    encoding_format: Literal["float", "base64"]
    """Format for the embeddings."""

    model: str
    """Model to use for embeddings."""
