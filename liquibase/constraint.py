# pylint: disable=C0103,R,C0114
from typing import Literal, Optional, TypedDict


class CheckConstraint(TypedDict):
    """Permitted attributes for `AddCheckConstraint.addCheckConstraint`."""

    catalogName: Optional[str]
    constraintBody: str
    constraintName: str
    disabled: Optional[bool]
    schemaName: Optional[str]
    tableName: str
    validate: Optional[bool]


class AddCheckConstraint(TypedDict):
    """Permitted attributes for change
    [addCheckConstraint](https://docs.liquibase.com/change-types/add-check-constraint.html).
    """

    addCheckConstraint: CheckConstraint


class DefaultValue(TypedDict):
    """Permitted attributes for `AddDefaultValue.defaultValue`."""

    catalogName: Optional[str]
    columnDataType: str
    columnName: str
    defaultValue: Optional[str]
    defaultValueBoolean: Optional[bool]
    defaultValueComputed: Optional[str]
    defaultValueConstraintName: Optional[str]
    defaultValueDate: Optional[str]
    defaultValueNumeric: Optional[int]
    defaultValueSequenceNext: Optional[str]
    schemaName: Optional[str]
    tableName: str


class AddDefaultValue(TypedDict):
    """Permitted attributes for change
    [addCheckConstraint](https://docs.liquibase.com/change-types/add-default-value.html).
    """

    addDefaultValue: DefaultValue


ForeignKeyAction = Literal[
    "CASCADE", "NO ACTION", "SET NULL", "SET DEFAULT", "RESTRICT"
]


class ForeignKeyConstraint(TypedDict):
    """Permitted attributes for `AddForeignKeyConstraint.addForeignKeyConstraint`."""

    baseColumnNames: str
    baseTableCatalogName: Optional[str]
    baseTableName: str
    baseTableSchemaName: Optional[str]
    constraintName: str
    deferrable: Optional[bool]
    initiallyDeferred: Optional[bool]
    onDelete: Optional[ForeignKeyAction]
    onUpdate: Optional[ForeignKeyAction]
    referencedColumnNames: str
    referencedTableCatalogName: Optional[str]
    referencedTableName: str
    referencedTableSchemaName: Optional[str]
    validate: Optional[bool]


class AddForeignKeyConstraint(TypedDict):
    # pylint: disable=C0301
    """Permitted attributes for change
    [addForeignKeyConstraint](https://docs.liquibase.com/change-types/add-foreign-key-constraint.html).
    """

    addForeignKeyConstraint: ForeignKeyConstraint


class NotNullConstraint(TypedDict):
    """Permitted attributes for `AddNotNullConstraint.addNotNullConstraint`."""

    catalogName: Optional[str]
    columnDataType: str
    columnName: str
    constraintName: Optional[str]
    defaultNullValue: Optional[str]
    schemaName: Optional[str]
    tableName: str
    validate: Optional[bool]


class AddNotNullConstraint(TypedDict):
    # pylint: disable=C0301
    """Permitted attributes for change
    [addNotNullConstraint](https://docs.liquibase.com/change-types/add-not-null-constraint.html).
    """

    addNotNullConstraint: NotNullConstraint


class PrimaryKey(TypedDict):
    """Permitted attributes for `AddPrimaryKey.addPrimaryKey`."""

    catalogName: Optional[str]
    clustered: Optional[bool]
    columnNames: str
    constraintName: Optional[str]
    forIndexCatalogName: Optional[str]
    forIndexName: Optional[str]
    forIndexSchemaName: Optional[str]
    schemaName: Optional[str]
    tableName: str
    tablespace: Optional[str]
    validate: Optional[bool]


class AddPrimaryKey(TypedDict):
    """Permitted attributes for change
    [addPrimaryKey](https://docs.liquibase.com/change-types/add-primary-key.html).
    """

    addPrimaryKey: PrimaryKey


class UniqueConstraint(TypedDict):
    """Permitted attributes for `AddUniqueConstraint.addUniqueConstraint`."""

    catalogName: Optional[str]
    clustered: Optional[bool]
    columnNames: str
    constraintName: Optional[str]
    deferrable: Optional[bool]
    disabled: Optional[bool]
    forIndexCatalogName: Optional[str]
    forIndexName: Optional[str]
    forIndexSchemaName: Optional[str]
    initiallyDeferred: Optional[bool]
    schemaName: Optional[str]
    tableName: Optional[str]
    tablespace: Optional[str]
    validate: Optional[bool]


class AddUniqueConstraint(TypedDict):
    """Permitted attributes for change
    [addUniqueConstraint](https://docs.liquibase.com/change-types/add-primary-key.html).
    """

    addUniqueConstraint: UniqueConstraint


class DisableCheckConstraintAttributes(TypedDict):
    """Permitted attributes for `DisableCheckConstraint.disableCheckConstraint`."""

    catalogName: Optional[str]
    constraintName: str
    schemaName: Optional[str]
    tableName: str


class DisableCheckConstraint(TypedDict):
    """Permitted attributes for change
    [disableCheckConstraint](https://docs.liquibase.com/change-types/disable-check-constraint.html).
    """

    disableCheckConstraint: DisableCheckConstraintAttributes
