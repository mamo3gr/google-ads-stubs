from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v20.resources.types.user_list_customer_type import (
    UserListCustomerType,
)

_M = TypeVar("_M")

class MutateUserListCustomerTypeResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name"]
    ) -> bool: ...

class MutateUserListCustomerTypesRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[UserListCustomerTypeOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[UserListCustomerTypeOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal["customer_id", "operations", "partial_failure", "validate_only"],
    ) -> bool: ...

class MutateUserListCustomerTypesResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateUserListCustomerTypeResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateUserListCustomerTypeResult] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["partial_failure_error", "results"]
    ) -> bool: ...

class UserListCustomerTypeOperation(proto.Message):
    create: UserListCustomerType
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        create: UserListCustomerType = ...,
        remove: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["create", "remove"]
    ) -> bool: ...
