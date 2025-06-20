import abc
from typing import Awaitable, Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v20.services.types import data_link_service

__all__ = ["DataLinkServiceTransport"]

class DataLinkServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        quota_project_id: str | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: bool | None = False,
        api_audience: str | None = None,
        **kwargs,
    ) -> None: ...
    @property
    def host(self): ...
    def close(self) -> None: ...
    @property
    def create_data_link(
        self,
    ) -> Callable[
        [data_link_service.CreateDataLinkRequest],
        data_link_service.CreateDataLinkResponse
        | Awaitable[data_link_service.CreateDataLinkResponse],
    ]: ...
    @property
    def remove_data_link(
        self,
    ) -> Callable[
        [data_link_service.RemoveDataLinkRequest],
        data_link_service.RemoveDataLinkResponse
        | Awaitable[data_link_service.RemoveDataLinkResponse],
    ]: ...
    @property
    def update_data_link(
        self,
    ) -> Callable[
        [data_link_service.UpdateDataLinkRequest],
        data_link_service.UpdateDataLinkResponse
        | Awaitable[data_link_service.UpdateDataLinkResponse],
    ]: ...
    @property
    def kind(self) -> str: ...
