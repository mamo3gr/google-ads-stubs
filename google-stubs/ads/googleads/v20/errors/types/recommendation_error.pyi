from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class RecommendationErrorEnum(proto.Message):
    class RecommendationError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BUDGET_AMOUNT_TOO_SMALL = 2
        BUDGET_AMOUNT_TOO_LARGE = 3
        INVALID_BUDGET_AMOUNT = 4
        POLICY_ERROR = 5
        INVALID_BID_AMOUNT = 6
        ADGROUP_KEYWORD_LIMIT = 7
        RECOMMENDATION_ALREADY_APPLIED = 8
        RECOMMENDATION_INVALIDATED = 9
        TOO_MANY_OPERATIONS = 10
        NO_OPERATIONS = 11
        DIFFERENT_TYPES_NOT_SUPPORTED = 12
        DUPLICATE_RESOURCE_NAME = 13
        RECOMMENDATION_ALREADY_DISMISSED = 14
        INVALID_APPLY_REQUEST = 15
        RECOMMENDATION_TYPE_APPLY_NOT_SUPPORTED = 17
        INVALID_MULTIPLIER = 18
        ADVERTISING_CHANNEL_TYPE_GENERATE_NOT_SUPPORTED = 19
        RECOMMENDATION_TYPE_GENERATE_NOT_SUPPORTED = 20
        RECOMMENDATION_TYPES_CANNOT_BE_EMPTY = 21
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_BIDDING_INFO = 22
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_BIDDING_STRATEGY_TYPE = 23
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_ASSET_GROUP_INFO = 24
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_ASSET_GROUP_INFO_WITH_FINAL_URL = (
            25
        )
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_COUNTRY_CODES_FOR_SEARCH_CHANNEL = 26
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_INVALID_COUNTRY_CODE_FOR_SEARCH_CHANNEL = 27
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_LANGUAGE_CODES_FOR_SEARCH_CHANNEL = 28
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_EITHER_POSITIVE_OR_NEGATIVE_LOCATION_IDS_FOR_SEARCH_CHANNEL = 29
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_AD_GROUP_INFO_FOR_SEARCH_CHANNEL = 30
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_KEYWORDS_FOR_SEARCH_CHANNEL = 31
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_WITH_CHANNEL_TYPE_SEARCH_AND_BIDDING_STRATEGY_TYPE_TARGET_IMPRESSION_SHARE_REQUIRES_LOCATION = 32
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_WITH_CHANNEL_TYPE_SEARCH_AND_BIDDING_STRATEGY_TYPE_TARGET_IMPRESSION_SHARE_REQUIRES_TARGET_IMPRESSION_SHARE_MICROS = 33
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_TARGET_IMPRESSION_SHARE_MICROS_BETWEEN_1_AND_1000000 = 34
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_WITH_CHANNEL_TYPE_SEARCH_AND_BIDDING_STRATEGY_TYPE_TARGET_IMPRESSION_SHARE_REQUIRES_TARGET_IMPRESSION_SHARE_INFO = 35
        MERCHANT_CENTER_ACCOUNT_ID_NOT_SUPPORTED_ADVERTISING_CHANNEL_TYPE = 36

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
