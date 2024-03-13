# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class RerankerDataMetrics(pydantic.BaseModel):
    num_train_queries: typing.Optional[str] = pydantic.Field(alias="numTrainQueries", default=None)
    """
    The number of training queries.
    """

    num_train_relevant_passages: typing.Optional[str] = pydantic.Field(alias="numTrainRelevantPassages", default=None)
    """
    The sum of all relevant passages of valid training examples.
    """

    num_train_hard_negatives: typing.Optional[str] = pydantic.Field(alias="numTrainHardNegatives", default=None)
    """
    The sum of all hard negatives of valid training examples.
    """

    num_eval_queries: typing.Optional[str] = pydantic.Field(alias="numEvalQueries", default=None)
    """
    The number of evaluation queries.
    """

    num_eval_relevant_passages: typing.Optional[str] = pydantic.Field(alias="numEvalRelevantPassages", default=None)
    """
    The sum of all relevant passages of valid eval examples.
    """

    num_eval_hard_negatives: typing.Optional[str] = pydantic.Field(alias="numEvalHardNegatives", default=None)
    """
    The sum of all hard negatives of valid eval examples.
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
        allow_population_by_field_name = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
