from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v20.enums.types.sk_ad_network_coarse_conversion_value import (
    SkAdNetworkCoarseConversionValueEnum,
)

_M = TypeVar("_M")

class CustomerSkAdNetworkConversionValueSchema(proto.Message):
    class SkAdNetworkConversionValueSchema(proto.Message):
        class CoarseGrainedConversionValueMappings(proto.Message):
            low_conversion_value_mapping: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping
            medium_conversion_value_mapping: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping
            high_conversion_value_mapping: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping
            def __init__(
                self: _M,
                mapping: _M | Mapping | google.protobuf.message.Message | None = None,
                *,
                ignore_unknown_fields: bool = False,
                low_conversion_value_mapping: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping = ...,
                medium_conversion_value_mapping: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping = ...,
                high_conversion_value_mapping: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping = ...,
            ) -> None: ...
            def __contains__(  # type: ignore[override]
                self,
                key: Literal[
                    "low_conversion_value_mapping",
                    "medium_conversion_value_mapping",
                    "high_conversion_value_mapping",
                ],
            ) -> bool: ...

        class ConversionValueMapping(proto.Message):
            min_time_post_install_hours: int
            max_time_post_install_hours: int
            mapped_events: MutableSequence[
                CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.Event
            ]
            def __init__(
                self: _M,
                mapping: _M | Mapping | google.protobuf.message.Message | None = None,
                *,
                ignore_unknown_fields: bool = False,
                min_time_post_install_hours: int = ...,
                max_time_post_install_hours: int = ...,
                mapped_events: MutableSequence[
                    CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.Event
                ] = ...,
            ) -> None: ...
            def __contains__(  # type: ignore[override]
                self,
                key: Literal[
                    "min_time_post_install_hours",
                    "max_time_post_install_hours",
                    "mapped_events",
                ],
            ) -> bool: ...

        class Event(proto.Message):
            class EventOccurrenceRange(proto.Message):
                min_event_count: int
                max_event_count: int
                def __init__(
                    self: _M,
                    mapping: _M
                    | Mapping
                    | google.protobuf.message.Message
                    | None = None,
                    *,
                    ignore_unknown_fields: bool = False,
                    min_event_count: int = ...,
                    max_event_count: int = ...,
                ) -> None: ...
                def __contains__(  # type: ignore[override]
                    self, key: Literal["min_event_count", "max_event_count"]
                ) -> bool: ...

            class RevenueRange(proto.Message):
                min_event_revenue: float
                max_event_revenue: float
                def __init__(
                    self: _M,
                    mapping: _M
                    | Mapping
                    | google.protobuf.message.Message
                    | None = None,
                    *,
                    ignore_unknown_fields: bool = False,
                    min_event_revenue: float = ...,
                    max_event_revenue: float = ...,
                ) -> None: ...
                def __contains__(  # type: ignore[override]
                    self, key: Literal["min_event_revenue", "max_event_revenue"]
                ) -> bool: ...

            mapped_event_name: str
            currency_code: str
            event_revenue_range: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.Event.RevenueRange
            event_revenue_value: float
            event_occurrence_range: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.Event.EventOccurrenceRange
            event_counter: int
            def __init__(
                self: _M,
                mapping: _M | Mapping | google.protobuf.message.Message | None = None,
                *,
                ignore_unknown_fields: bool = False,
                mapped_event_name: str = ...,
                currency_code: str = ...,
                event_revenue_range: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.Event.RevenueRange = ...,
                event_revenue_value: float = ...,
                event_occurrence_range: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.Event.EventOccurrenceRange = ...,
                event_counter: int = ...,
            ) -> None: ...
            def __contains__(  # type: ignore[override]
                self,
                key: Literal[
                    "mapped_event_name",
                    "currency_code",
                    "event_revenue_range",
                    "event_revenue_value",
                    "event_occurrence_range",
                    "event_counter",
                ],
            ) -> bool: ...

        class FineGrainedConversionValueMappings(proto.Message):
            fine_grained_conversion_value: int
            conversion_value_mapping: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping
            def __init__(
                self: _M,
                mapping: _M | Mapping | google.protobuf.message.Message | None = None,
                *,
                ignore_unknown_fields: bool = False,
                fine_grained_conversion_value: int = ...,
                conversion_value_mapping: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping = ...,
            ) -> None: ...
            def __contains__(  # type: ignore[override]
                self,
                key: Literal[
                    "fine_grained_conversion_value", "conversion_value_mapping"
                ],
            ) -> bool: ...

        class PostbackMapping(proto.Message):
            postback_sequence_index: int
            coarse_grained_conversion_value_mappings: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.CoarseGrainedConversionValueMappings
            lock_window_coarse_conversion_value: (
                SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue
            )
            lock_window_fine_conversion_value: int
            lock_window_event: str
            def __init__(
                self: _M,
                mapping: _M | Mapping | google.protobuf.message.Message | None = None,
                *,
                ignore_unknown_fields: bool = False,
                postback_sequence_index: int = ...,
                coarse_grained_conversion_value_mappings: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.CoarseGrainedConversionValueMappings = ...,
                lock_window_coarse_conversion_value: SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue = ...,
                lock_window_fine_conversion_value: int = ...,
                lock_window_event: str = ...,
            ) -> None: ...
            def __contains__(  # type: ignore[override]
                self,
                key: Literal[
                    "postback_sequence_index",
                    "coarse_grained_conversion_value_mappings",
                    "lock_window_coarse_conversion_value",
                    "lock_window_fine_conversion_value",
                    "lock_window_event",
                ],
            ) -> bool: ...

        app_id: str
        measurement_window_hours: int
        fine_grained_conversion_value_mappings: MutableSequence[
            CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.FineGrainedConversionValueMappings
        ]
        postback_mappings: MutableSequence[
            CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.PostbackMapping
        ]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            app_id: str = ...,
            measurement_window_hours: int = ...,
            fine_grained_conversion_value_mappings: MutableSequence[
                CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.FineGrainedConversionValueMappings
            ] = ...,
            postback_mappings: MutableSequence[
                CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.PostbackMapping
            ] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "app_id",
                "measurement_window_hours",
                "fine_grained_conversion_value_mappings",
                "postback_mappings",
            ],
        ) -> bool: ...

    resource_name: str
    schema: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        schema: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "schema"]
    ) -> bool: ...
