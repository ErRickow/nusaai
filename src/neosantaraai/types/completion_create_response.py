# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .usage import Usage
from .._models import BaseModel
from .metadata import Metadata

__all__ = ["CompletionCreateResponse", "Choice"]


class Choice(BaseModel):
    finish_reason: Optional[Literal["stop", "length", "content_filter"]] = None

    index: Optional[int] = None

    logprobs: Optional[object] = None

    text: Optional[str] = None


class CompletionCreateResponse(BaseModel):
    id: Optional[str] = None

    choices: Optional[List[Choice]] = None

    created: Optional[int] = None

    info_metadata: Optional[Metadata] = None

    model: Optional[str] = None

    object: Optional[str] = None

    usage: Optional[Usage] = None
