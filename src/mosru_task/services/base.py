from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Any,
    Dict,
)

from mosru_task.enums import ServiceResultStatus


@dataclass
class ServiceResult:
    status: str = ServiceResultStatus.Ok
    data: Dict[str, Any] = field(default_factory=dict)
