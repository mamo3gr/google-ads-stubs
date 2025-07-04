from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AdTypeEnum(proto.Message):
    class AdType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        TEXT_AD = 2
        EXPANDED_TEXT_AD = 3
        EXPANDED_DYNAMIC_SEARCH_AD = 7
        HOTEL_AD = 8
        SHOPPING_SMART_AD = 9
        SHOPPING_PRODUCT_AD = 10
        VIDEO_AD = 12
        IMAGE_AD = 14
        RESPONSIVE_SEARCH_AD = 15
        LEGACY_RESPONSIVE_DISPLAY_AD = 16
        APP_AD = 17
        LEGACY_APP_INSTALL_AD = 18
        RESPONSIVE_DISPLAY_AD = 19
        LOCAL_AD = 20
        HTML5_UPLOAD_AD = 21
        DYNAMIC_HTML5_AD = 22
        APP_ENGAGEMENT_AD = 23
        SHOPPING_COMPARISON_LISTING_AD = 24
        VIDEO_BUMPER_AD = 25
        VIDEO_NON_SKIPPABLE_IN_STREAM_AD = 26
        VIDEO_TRUEVIEW_IN_STREAM_AD = 29
        VIDEO_RESPONSIVE_AD = 30
        SMART_CAMPAIGN_AD = 31
        CALL_AD = 32
        APP_PRE_REGISTRATION_AD = 33
        IN_FEED_VIDEO_AD = 34
        DEMAND_GEN_MULTI_ASSET_AD = 40
        DEMAND_GEN_CAROUSEL_AD = 41
        TRAVEL_AD = 37
        DEMAND_GEN_VIDEO_RESPONSIVE_AD = 42
        DEMAND_GEN_PRODUCT_AD = 39
        YOUTUBE_AUDIO_AD = 44

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
