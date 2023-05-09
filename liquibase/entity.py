# pylint: disable=C0103,R,C0114
from typing import List, Literal, Optional, TypedDict


class AutoIncrement(TypedDict):
    """Permitted attributes for `AddAutoIncrement.addAutoIncrement`."""

    catalogName: Optional[str]
    columnDataType: str
    columnName: str
    defaultOnNull: Optional[str]
    generationType: Optional[str]
    incrementBy: Optional[int]
    schemaName: Optional[str]
    startWith: Optional[str]
    tableName: Optional[str]


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

    catalogName: Optional[str]
    columns: List[Column]
    schemaName: Optional[str]
    tableName: str


class Sequence(TypedDict):
    """Permitted attributes for `AlterSequence.alterSequence`."""

    cacheSize: Optional[int]
    catalogName: Optional[str]
    cycle: Optional[bool]
    dataType: Optional[str]
    incrementBy: Optional[int]
    maxValue: Optional[int]
    minValue: Optional[int]
    ordered: Optional[bool]
    schemaName: Optional[str]
    sequenceName: str


class AlterSequence(TypedDict):
    """Permitted attributes for change
    [alterSequence](https://docs.liquibase.com/change-types/alter-sequence.html)."""

    alterSequence: Sequence


class Function(TypedDict):
    """Permitted attributes for `CreateFunction.createFunction`."""

    catalogName: Optional[str]
    dbms: Optional[str]
    encoding: Optional[str]
    functionBody: str
    functionName: str
    path: str
    procedureText: str
    relativeToChangelogFile: Optional[bool]
    replaceIfExists: Optional[bool]
    schemaName: Optional[str]


class CreateFunction(TypedDict):
    """Permitted attributes for change
    [createFunction](https://docs.liquibase.com/change-types/create-function.html)."""

    createFunction: Function


class IndexColumn(TypedDict):
    """Permitted attributes for `Index.columns[.]`,"""

    computed: Optional[bool]
    descending: Optional[bool]
    name: str


class Index(TypedDict):
    """Permitted attributes for `CreateIndex.createIndex`."""

    catalogName: Optional[str]
    clustered: Optional[bool]
    column: IndexColumn
    indexName: str
    schemaName: Optional[str]
    tableName: str
    tablespace: Optional[str]
    unique: Optional[bool]


class CreateIndex(TypedDict):
    """Permitted attributes for change
    [createIndex](https://docs.liquibase.com/change-types/create-index.html)."""

    createIndex: Index


class Package(TypedDict):
    """Permitted attributes for `CreatePackage.createPackage`."""

    catalogName: Optional[str]
    dbms: Optional[str]
    encoding: Optional[str]
    packageName: str
    packageText: str
    path: str
    procedureText: str
    relativeToChangelogFile: Optional[bool]
    replaceIfExists: Optional[bool]
    schemaName: Optional[str]


class CreatePackage(TypedDict):
    """Permitted attributes for change
    [createPackage](https://docs.liquibase.com/change-types/create-package.html)."""

    createPackage: Package


class PackageBody(TypedDict):
    """Permitted attributes for `CreatePackageBody.createPackageBody`."""

    catalogName: Optional[str]
    dbms: Optional[str]
    encoding: Optional[str]
    packageBodyName: str
    packageBodyText: str
    path: str
    relativeToChangelogFile: Optional[bool]
    replaceIfExists: Optional[bool]
    schemaName: Optional[str]


class CreatePackageBody(TypedDict):
    """Permitted attributes for change
    [createPackageBody](https://docs.liquibase.com/change-types/create-package-body.html).
    """

    createPackageBody: PackageBody


class Procedure(TypedDict):
    """Permitted attributes for `CreateProcedure.createProcedure`."""

    catalogName: Optional[str]
    dbms: Optional[str]
    encoding: Optional[str]
    path: str
    procedureName: str
    procedureText: str
    relativeToChangelogFile: Optional[bool]
    replaceIfExists: Optional[bool]
    schemaName: Optional[str]


class CreateProcedure(TypedDict):
    """Permitted attributes for change
    [createProcedure](https://docs.liquibase.com/change-types/create-procedure.html).
    """

    createProcedure: Procedure


class CreateSequence(TypedDict):
    """Permitted attributes for change
    [createSequence](https://docs.liquibase.com/change-types/create-sequence.html).
    """

    createSequence: Sequence


class Synonym(TypedDict):
    """Permitted attributes for `CreateSynonym.createSynonym`."""

    objectCatalogName: Optional[str]
    objectName: str
    objectSchemaName: Optional[str]
    objectType: str
    private: bool
    replaceIfExists: Optional[bool]
    synonymCatalogName: Optional[str]
    synonymName: str
    synonymSchemaName: Optional[str]


class CreateSynonym(TypedDict):
    """Permitted attributes for change
    [createSynonym](https://docs.liquibase.com/change-types/create-synonym.html).
    """

    createSynonym: Synonym


class TableColumn(TypedDict):
    """Permitted attributes for `CreateTable.columns[*]`."""

    column: Column


class Table(TypedDict):
    """Permitted attributes for `CreateTable.createTable`."""

    catalogName: Optional[str]
    columns: List[TableColumn]
    remarks: Optional[str]
    schemaName: Optional[str]
    tableName: str
    tablespace: Optional[str]


class CreateTable(TypedDict):
    """Permitted attributes for change
    [createTable](https://docs.liquibase.com/change-types/create-table.html)."""

    createTable: Table


class Trigger(TypedDict):
    """Permitted attributes for `CreateTrigger.createTrigger`."""

    catalogName: Optional[str]
    dbms: Optional[str]
    disabled: Optional[bool]
    encoding: Optional[str]
    path: Optional[str]
    procedureText: str
    relativeToChangelogFile: Optional[bool]
    replaceIfExists: Optional[bool]
    schemaName: Optional[str]
    scope: Optional[str]
    tableName: Optional[str]
    triggerBody: str
    triggerName: str


class CreateTrigger(TypedDict):
    """Permitted attributes for change
    [createTrigger](https://docs.liquibase.com/change-types/create-trigger.html)."""

    createTrigger: Trigger


ReplaceIfExists = Literal["CREATE", "REPLACE"]


class View(TypedDict):
    """Permitted attributes for `CreateView.createView`."""

    catalogName: Optional[str]
    encoding: Optional[str]
    fullDefinition: Optional[bool]
    path: Optional[str]
    relativeToChangelogFile: Optional[bool]
    remarks: Optional[str]
    replaceIfExists: ReplaceIfExists
    schemaName: Optional[str]
    selectQuery: str
    viewName: str


class CreateView(TypedDict):
    """Permitted attributes for change
    [createView](https://docs.liquibase.com/change-types/create-view.html)."""

    view: View
