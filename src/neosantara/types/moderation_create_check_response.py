# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .metadata import Metadata

__all__ = ["ModerationCreateCheckResponse", "Result", "ResultCategories", "ResultCategoryScores"]


class ResultCategories(BaseModel):
    harassment: Optional[bool] = None

    harassment_threatening: Optional[bool] = FieldInfo(alias="harassment/threatening", default=None)

    hate: Optional[bool] = None

    hate_threatening: Optional[bool] = FieldInfo(alias="hate/threatening", default=None)

    self_harm: Optional[bool] = FieldInfo(alias="self-harm", default=None)

    self_harm_instructions: Optional[bool] = FieldInfo(alias="self-harm/instructions", default=None)

    self_harm_intent: Optional[bool] = FieldInfo(alias="self-harm/intent", default=None)

    sexual: Optional[bool] = None

    sexual_minors: Optional[bool] = FieldInfo(alias="sexual/minors", default=None)

    violence: Optional[bool] = None

    violence_graphic: Optional[bool] = FieldInfo(alias="violence/graphic", default=None)


class ResultCategoryScores(BaseModel):
    harassment: Optional[float] = None

    harassment_threatening: Optional[float] = FieldInfo(alias="harassment/threatening", default=None)

    hate: Optional[float] = None

    hate_threatening: Optional[float] = FieldInfo(alias="hate/threatening", default=None)

    self_harm: Optional[float] = FieldInfo(alias="self-harm", default=None)

    self_harm_instructions: Optional[float] = FieldInfo(alias="self-harm/instructions", default=None)

    self_harm_intent: Optional[float] = FieldInfo(alias="self-harm/intent", default=None)

    sexual: Optional[float] = None

    sexual_minors: Optional[float] = FieldInfo(alias="sexual/minors", default=None)

    violence: Optional[float] = None

    violence_graphic: Optional[float] = FieldInfo(alias="violence/graphic", default=None)


class Result(BaseModel):
    categories: Optional[ResultCategories] = None
    """Category flags for different types of harmful content."""

    category_scores: Optional[ResultCategoryScores] = None
    """Confidence scores for each category (0-1)."""

    flagged: Optional[bool] = None
    """Whether the content was flagged."""


class ModerationCreateCheckResponse(BaseModel):
    id: Optional[str] = None

    api_metadata: Optional[Metadata] = FieldInfo(alias="_metadata", default=None)

    model: Optional[str] = None

    results: Optional[List[Result]] = None
