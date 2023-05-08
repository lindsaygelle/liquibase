# pylint: disable=C0103,R,C0114
from typing import Literal, TypedDict


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


ForeignKeyAction = Literal[
    "CASCADE", "NO ACTION", "SET NULL", "SET DEFAULT", "RESTRICT"
]


class ForeignKeyConstraint(TypedDict):
    """Permitted attributes for `AddForeignKeyConstraint.addForeignKeyConstraint`."""

    baseColumnNames: str
    baseTableCatalogName: str
    baseTableName: str
    baseTableSchemaName: str
    constraintName: str
    deferrable: bool
    foreignKeyName: str
    initiallyDeferred: bool
    onDelete: ForeignKeyAction
    onUpdate: ForeignKeyAction
    referencedColumnNames: str
    referencedTableCatalogName: str
    referencedTableName: str
    referencedTableSchemaName: str
    validate: bool


class AddForeignKeyConstraint(TypedDict):
    # pylint: disable=C0301
    """Permitted attributes for change
    [addForeignKeyConstraint](https://docs.liquibase.com/change-types/add-foreign-key-constraint.html).
    """

    addForeignKeyConstraint: ForeignKeyConstraint


class NotNullConstraint(TypedDict):
    """Permitted attributes for `AddNotNullConstraint.addNotNullConstraint`."""

    catalogName: str
    columnDataType: str
    columnName: str
    constraintName: str
    defaultNullValue: str
    schemaName: str
    tableName: str
    validate: bool


class AddNotNullConstraint(TypedDict):
    # pylint: disable=C0301
    """Permitted attributes for change
    [addNotNullConstraint](https://docs.liquibase.com/change-types/add-not-null-constraint.html).
    """

    addNotNullConstraint: NotNullConstraint


class PrimaryKey(TypedDict):
    """Permitted attributes for `AddPrimaryKey.addPrimaryKey`."""

    catalogName: str
    clustered: bool
    columnNames: str
    constraintName: str
    forIndexCatalogName: str
    forIndexName: str
    forIndexSchemaName: str
    schemaName: str
    tableName: str
    tablespace: str
    validate: bool


class AddPrimaryKey(TypedDict):
    """Permitted attributes for change
    [addPrimaryKey](https://docs.liquibase.com/change-types/add-primary-key.html).
    """

    addPrimaryKey: PrimaryKey


class UniqueConstraint(TypedDict):
    """Permitted attributes for `AddUniqueConstraint.addUniqueConstraint`."""

    catalogName: str
    clustered: bool
    columnNames: str
    constraintName: str
    deferrable: bool
    disabled: bool
    forIndexCatalogName: str
    forIndexName: str
    forIndexSchemaName: str
    initiallyDeferred: bool
    schemaName: str
    tableName: str
    tablespace: str
    validate: bool


class AddUniqueConstraint(TypedDict):
    """Permitted attributes for change
    [addUniqueConstraint](https://docs.liquibase.com/change-types/add-primary-key.html).
    """

    addUniqueConstraint: UniqueConstraint
