# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EmbedRequestEmbeddingTypesItem(str, enum.Enum):
    FLOAT = "float"
    INT_8 = "int8"
    UINT_8 = "uint8"
    BINARY = "binary"
    UBINARY = "ubinary"

    def visit(
        self,
        float_: typing.Callable[[], T_Result],
        int_8: typing.Callable[[], T_Result],
        uint_8: typing.Callable[[], T_Result],
        binary: typing.Callable[[], T_Result],
        ubinary: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EmbedRequestEmbeddingTypesItem.FLOAT:
            return float_()
        if self is EmbedRequestEmbeddingTypesItem.INT_8:
            return int_8()
        if self is EmbedRequestEmbeddingTypesItem.UINT_8:
            return uint_8()
        if self is EmbedRequestEmbeddingTypesItem.BINARY:
            return binary()
        if self is EmbedRequestEmbeddingTypesItem.UBINARY:
            return ubinary()
