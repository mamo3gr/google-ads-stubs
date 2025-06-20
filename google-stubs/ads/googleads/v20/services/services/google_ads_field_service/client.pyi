import types
from typing import Callable, Dict, Sequence, Tuple, Type

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v20.resources.types import google_ads_field
from google.ads.googleads.v20.services.services.google_ads_field_service import pagers
from google.ads.googleads.v20.services.types import google_ads_field_service

from .transports.base import GoogleAdsFieldServiceTransport

__all__ = ["GoogleAdsFieldServiceClient"]

class GoogleAdsFieldServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[GoogleAdsFieldServiceTransport]: ...

class GoogleAdsFieldServiceClient(metaclass=GoogleAdsFieldServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> GoogleAdsFieldServiceTransport: ...
    @staticmethod
    def google_ads_field_path(google_ads_field: str) -> str: ...
    @staticmethod
    def parse_google_ads_field_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_billing_account_path(billing_account: str) -> str: ...
    @staticmethod
    def parse_common_billing_account_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_folder_path(folder: str) -> str: ...
    @staticmethod
    def parse_common_folder_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_organization_path(organization: str) -> str: ...
    @staticmethod
    def parse_common_organization_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_project_path(project: str) -> str: ...
    @staticmethod
    def parse_common_project_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_location_path(project: str, location: str) -> str: ...
    @staticmethod
    def parse_common_location_path(path: str) -> dict[str, str]: ...
    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: client_options_lib.ClientOptions | None = None
    ): ...
    @property
    def api_endpoint(self): ...
    @property
    def universe_domain(self) -> str: ...
    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials | None = None,
        transport: str
        | GoogleAdsFieldServiceTransport
        | Callable[..., GoogleAdsFieldServiceTransport]
        | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    def get_google_ads_field(
        self,
        request: google_ads_field_service.GetGoogleAdsFieldRequest | dict | None = None,
        *,
        resource_name: str | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> google_ads_field.GoogleAdsField: ...
    def search_google_ads_fields(
        self,
        request: google_ads_field_service.SearchGoogleAdsFieldsRequest
        | dict
        | None = None,
        *,
        query: str | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> pagers.SearchGoogleAdsFieldsPager: ...
    def __enter__(self) -> GoogleAdsFieldServiceClient: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
