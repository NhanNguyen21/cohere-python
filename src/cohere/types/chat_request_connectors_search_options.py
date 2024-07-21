# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from ..core.unchecked_base_model import UncheckedBaseModel


class ChatRequestConnectorsSearchOptions(UncheckedBaseModel):
    """
    (internal) Sets inference and model options for RAG search query and tool use generations. Defaults are used when options are not specified here, meaning that other parameters outside of connectors_search_options are ignored (such as model= or temperature=).
    """

    seed: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    If specified, the backend will make a best effort to sample tokens
    deterministically, such that repeated requests with the same
    seed and parameters should return the same result. However,
    determinism cannot be totally guaranteed.
    Compatible Deployments: Cohere Platform, Azure, AWS Sagemaker/Bedrock, Private Deployments
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
