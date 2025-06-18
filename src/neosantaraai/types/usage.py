# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Usage"]


class Usage(BaseModel):
    completion_tokens: Optional[int] = None
    """Tokens in the completion."""

    prompt_tokens: Optional[int] = None
    """Tokens in the prompt."""

    total_tokens: Optional[int] = None
    """Total tokens used."""
