# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .chat_citation import ChatCitation
from .chat_document import ChatDocument
from .chat_search_query import ChatSearchQuery
from .chat_search_result import ChatSearchResult

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class NonStreamedChatResponse(pydantic.BaseModel):
    text: str = pydantic.Field(description="Contents of the reply generated by the model.")
    generation_id: str = pydantic.Field(
        description="Unique identifier for the generated reply. Useful for submitting feedback."
    )
    citations: typing.Optional[typing.List[ChatCitation]] = pydantic.Field(
        description="Inline citations for the generated reply."
    )
    documents: typing.Optional[typing.List[ChatDocument]] = pydantic.Field(
        description="Documents seen by the model when generating the reply."
    )
    search_queries: typing.Optional[typing.List[ChatSearchQuery]] = pydantic.Field(
        description="Generated search queries, meant to be used as part of the RAG flow."
    )
    search_results: typing.Optional[typing.List[ChatSearchResult]] = pydantic.Field(
        description="Documents retrieved from each of the conducted searches."
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}