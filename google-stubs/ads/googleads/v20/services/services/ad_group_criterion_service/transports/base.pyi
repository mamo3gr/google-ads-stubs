import abc
from typing import Awaitable, Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v20.services.types import ad_group_criterion_service

__all__ = ["AdGroupCriterionServiceTransport"]

class AdGroupCriterionServiceTransport(abc.ABC):
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
    def mutate_ad_group_criteria(
        self,
    ) -> Callable[
        [ad_group_criterion_service.MutateAdGroupCriteriaRequest],
        ad_group_criterion_service.MutateAdGroupCriteriaResponse
        | Awaitable[ad_group_criterion_service.MutateAdGroupCriteriaResponse],
    ]: ...
    @property
    def kind(self) -> str: ...
