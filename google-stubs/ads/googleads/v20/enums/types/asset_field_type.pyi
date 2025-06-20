from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AssetFieldTypeEnum(proto.Message):
    class AssetFieldType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        HEADLINE = 2
        DESCRIPTION = 3
        MANDATORY_AD_TEXT = 4
        MARKETING_IMAGE = 5
        MEDIA_BUNDLE = 6
        YOUTUBE_VIDEO = 7
        BOOK_ON_GOOGLE = 8
        LEAD_FORM = 9
        PROMOTION = 10
        CALLOUT = 11
        STRUCTURED_SNIPPET = 12
        SITELINK = 13
        MOBILE_APP = 14
        HOTEL_CALLOUT = 15
        CALL = 16
        PRICE = 24
        LONG_HEADLINE = 17
        BUSINESS_NAME = 18
        SQUARE_MARKETING_IMAGE = 19
        PORTRAIT_MARKETING_IMAGE = 20
        LOGO = 21
        LANDSCAPE_LOGO = 22
        VIDEO = 23
        CALL_TO_ACTION_SELECTION = 25
        AD_IMAGE = 26
        BUSINESS_LOGO = 27
        HOTEL_PROPERTY = 28
        DEMAND_GEN_CAROUSEL_CARD = 30
        BUSINESS_MESSAGE = 31
        TALL_PORTRAIT_MARKETING_IMAGE = 32

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
