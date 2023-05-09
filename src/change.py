# pylint: disable=C0103,R,C0114
from dataclasses import dataclass
from typing import Any, Dict, TypedDict


@dataclass
class CustomChange(TypedDict):
    """Permitted attributes for change
    [customChange](https://docs.liquibase.com/change-types/custom-change.html).
    """

    customChange: Dict[str, Any]
