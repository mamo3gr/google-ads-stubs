import types
from typing import Callable, Dict, MutableSequence, Sequence, Tuple, Type

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v20.services.types import campaign_service

from .transports.base import CampaignServiceTransport

__all__ = ["CampaignServiceClient"]

class CampaignServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[CampaignServiceTransport]: ...

class CampaignServiceClient(metaclass=CampaignServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> CampaignServiceTransport: ...
    @staticmethod
    def accessible_bidding_strategy_path(
        customer_id: str, bidding_strategy_id: str
    ) -> str: ...
    @staticmethod
    def parse_accessible_bidding_strategy_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def asset_set_path(customer_id: str, asset_set_id: str) -> str: ...
    @staticmethod
    def parse_asset_set_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def bidding_strategy_path(customer_id: str, bidding_strategy_id: str) -> str: ...
    @staticmethod
    def parse_bidding_strategy_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_path(customer_id: str, campaign_id: str) -> str: ...
    @staticmethod
    def parse_campaign_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_budget_path(customer_id: str, campaign_budget_id: str) -> str: ...
    @staticmethod
    def parse_campaign_budget_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_group_path(customer_id: str, campaign_group_id: str) -> str: ...
    @staticmethod
    def parse_campaign_group_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_label_path(
        customer_id: str, campaign_id: str, label_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_label_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def conversion_action_path(customer_id: str, conversion_action_id: str) -> str: ...
    @staticmethod
    def parse_conversion_action_path(path: str) -> dict[str, str]: ...
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
        | CampaignServiceTransport
        | Callable[..., CampaignServiceTransport]
        | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    def mutate_campaigns(
        self,
        request: campaign_service.MutateCampaignsRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        operations: MutableSequence[campaign_service.CampaignOperation] | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> campaign_service.MutateCampaignsResponse: ...
    def enable_p_max_brand_guidelines(
        self,
        request: campaign_service.EnablePMaxBrandGuidelinesRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        operations: MutableSequence[campaign_service.EnableOperation] | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> campaign_service.EnablePMaxBrandGuidelinesResponse: ...
    def __enter__(self) -> CampaignServiceClient: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
