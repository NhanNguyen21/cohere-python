# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .single_generation_token_likelihoods_item import SingleGenerationTokenLikelihoodsItem

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class SingleGeneration(pydantic.BaseModel):
    id: str
    text: str
    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    Refers to the nth generation. Only present when `num_generations` is greater than zero.
    """

    likelihood: typing.Optional[float] = None
    token_likelihoods: typing.Optional[typing.List[SingleGenerationTokenLikelihoodsItem]] = pydantic.Field(default=None)
    """
    Only returned if `return_likelihoods` is set to `GENERATION` or `ALL`. The likelihood refers to the average log-likelihood of the entire specified string, which is useful for [evaluating the performance of your model](likelihood-eval), especially if you've created a [custom model](/docs/training-custom-models). Individual token likelihoods provide the log-likelihood of each token. The first token will not have a likelihood.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}