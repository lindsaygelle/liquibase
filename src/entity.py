# pylint: disable=C0103,R,C0114
from typing import List, TypedDict


class AutoIncrement(TypedDict):
    """Permitted attributes for `AddAutoIncrement.addAutoIncrement`."""

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


class AddAutoIncrement(TypedDict):
    """Permitted attributes for change
    [addAutoIncrement](https://docs.liquibase.com/change-types/add-auto-increment.html).
    """

    addAutoIncrement: AutoIncrement


class ColumnConstraint(TypedDict):
    """Permitted attributes for `Column.constraints`."""

    checkConstraint: bool
    deferrable: bool
    deleteCascade: bool
    foreignKeyName: str
    initiallyDeferred: bool
    notNullConstraintName: str
    nullable: bool
    primaryKey: bool
    primaryKeyName: str
    primaryKeyTablespace: str
    referencedColumnNames: str
    referencedTableCatalogName: str
    referencedTableName: str
    referencedTableSchemaName: str
    references: str
    unique: str
    uniqueConstraintName: str
    validateForeignKey: bool
    validateNullable: bool
    validatePrimaryKey: bool
    validateUnique: bool


class Column(TypedDict):
    """Permitted attributes for `AddColumn.column`."""

    afterColumn: str
    autoIncrement: bool
    beforeColumn: str
    computed: bool
    constraints: ColumnConstraint
    defaultValue: str
    defaultValueBoolean: bool
    defaultValueComputed: str
    defaultValueConstraintName: str
    defaultValueDate: str
    defaultValueNumeric: int
    descending: bool
    encoding: str
    incrementBy: int
    name: str
    position: int
    remarks: str
    startWith: str
    type: str
    value: str
    valueBlobFile: str
    valueBoolean: bool
    valueClobFile: str
    valueComputed: str
    valueDate: str
    valueNumeric: int


class AddColumn(TypedDict):
    """Permitted attributes for change
    [addColumn](https://docs.liquibase.com/change-types/add-column.html)."""

    catalogName: str
    columns: List[Column]
    schemaName: str
    tableName: str


class Function(TypedDict):
    """Permitted attributes for `CreateFunction.createFunction`."""

    catalogName: str
    dbms: str
    encoding: str
    functionBody: str
    functionName: str
    path: str
    procedureText: str
    relativeToChangelogFile: bool
    replaceIfExists: bool
    schemaName: str


class CreateFunction(TypedDict):
    """Permitted attributes for change
    [createFunction](https://docs.liquibase.com/change-types/create-function.html)."""

    createFunction: Function


class IndexColumn(TypedDict):
    """Permitted attributes for `Index.columns[.]`,"""

    computed: bool
    descending: bool
    name: str


class Index(TypedDict):
    """Permitted attributes for `CreateIndex.createIndex`."""

    catalogName: str
    clustered: bool
    indexName: str
    schemaName: str
    tableName: str
    tablespace: str
    unique: bool


class CreateIndex(TypedDict):
    """Permitted attributes for change
    [createIndex](https://docs.liquibase.com/change-types/create-index.html)."""

    createIndex: Index


class TableColumn(TypedDict):
    """Permitted attributes for `CreateTable.columns[*]`."""

    column: Column


class Table(TypedDict):
    """Permitted attributes for change
    [createTable](https://docs.liquibase.com/change-types/create-table.html)."""

    catalogName: str
    columns: List[TableColumn]
    remarks: str
    schemaName: str
    tableName: str


class View(TypedDict):
    """Permitted attributes for `CreateView.createView`."""

    catalogName: str
    encoding: str
    fullDefinition: bool
    path: str
    relativeToChangelogFile: bool
    remarks: str
    replaceIfExists: bool
    schemaName: str
    selectQuery: str
    viewName: str


class CreateView(TypedDict):
    """Permitted attributes for change
    [createView](https://docs.liquibase.com/change-types/create-view.html)."""

    views: List[View]
