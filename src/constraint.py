# pylint: disable=C0114
from typing import TypedDict


class CheckConstraint(TypedDict):
    """Permitted attributes for `AddCheckConstraint.addCheckConstraint`."""

    catalogName: str
    constraintBody: str
    constraintName: str
    disabled: bool
    schemaName: str
    tableName: str
    validate: bool


class AddCheckConstraint(TypedDict):
    """Permitted attributes for change
    [addCheckConstraint](https://docs.liquibase.com/change-types/add-check-constraint.html).
    """

    addCheckConstraint: CheckConstraint
