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
    tableName: str


class AddAutoIncrement(TypedDict):
    """Permitted attributes for change
    [addAutoIncrement](https://docs.liquibase.com/change-types/add-auto-increment.html).
    """

    addAutoIncrement: AutoIncrement


class ColumnConstraintGenerated(TypedDict):
    """Permitted attributes for `ColumnConstraint.generated`."""

    onUpdate: Optional[bool]


class ColumnConstraint(TypedDict):
    """Permitted attributes for `Column.constraints`."""

    checkConstraint: Optional[bool]
    deferrable: Optional[bool]
    deleteCascade: Optional[bool]
    foreignKeyName: Optional[str]
    generated: Optional[ColumnConstraintGenerated]
    initiallyDeferred: Optional[bool]
    notNullConstraintName: Optional[str]
    nullable: Optional[bool]
    primaryKey: Optional[bool]
    primaryKeyName: Optional[str]
    primaryKeyTablespace: Optional[str]
    referencedColumnNames: Optional[str]
    referencedTableCatalogName: Optional[str]
    referencedTableName: Optional[str]
    referencedTableSchemaName: Optional[str]
    references: Optional[str]
    unique: Optional[str]
    uniqueConstraintName: Optional[str]
    validateForeignKey: Optional[bool]
    validateNullable: Optional[bool]
    validatePrimaryKey: Optional[bool]
    validateUnique: Optional[bool]


class ColumnAttributes(TypedDict):
    """Permitted attributes for `Column.column`."""

    afterColumn: Optional[str]
    autoIncrement: Optional[bool]
    beforeColumn: Optional[str]
    computed: Optional[bool]
    constraints: Optional[ColumnConstraint]
    defaultValue: Optional[str]
    defaultValueBoolean: Optional[bool]
    defaultValueComputed: Optional[str]
    defaultValueConstraintName: Optional[str]
    defaultValueDate: Optional[str]
    defaultValueNumeric: Optional[int]
    descending: Optional[bool]
    encoding: Optional[str]
    incrementBy: Optional[int]
    name: str
    position: Optional[int]
    remarks: Optional[str]
    startWith: Optional[str]
    type: str
    value: str
    valueBlobFile: Optional[str]
    valueBoolean: Optional[bool]
    valueClobFile: Optional[str]
    valueComputed: Optional[str]
    valueDate: Optional[str]
    valueNumeric: Optional[int]


class Column(TypedDict):
    """Permitted attributes for `AddColumnAttributes.columns[*]`."""

    column: ColumnAttributes


class AddColumnAttributes(TypedDict):
    """Permitted attributes for `AddColumn.addColumn`."""

    catalogName: Optional[str]
    columns: List[Column]
    schemaName: Optional[str]
    tableName: str


class AddColumn(TypedDict):
    """Permitted attributes for change
    [addColumn](https://docs.liquibase.com/change-types/add-column.html)."""

    addColumn: AddColumnAttributes


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


class Table(TypedDict):
    """Permitted attributes for `CreateTable.createTable`."""

    catalogName: Optional[str]
    columns: List[Column]
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


class DisableTriggerAttributes(TypedDict):
    """Permitted attributes for `DisableTrigger.disableTrigger`."""

    catalogName: Optional[str]
    schemaName: Optional[str]
    scope: Optional[str]
    tableName: Optional[str]
    triggerName: str


class DisableTrigger(TypedDict):
    """Permitted attributes for change
    [disableTrigger](https://docs.liquibase.com/change-types/disable-trigger.html)."""

    disableTrigger: DisableTriggerAttributes


class DropColumnAttributes(TypedDict):
    """Permitted attributes for `DropColumn.dropColumn`."""

    catalogName: Optional[str]
    columns: Optional[List[Column]]
    columnName: Optional[str]
    schemaName: Optional[str]
    tableName: str


class DropColumn(TypedDict):
    """Permitted attributes for change
    [dropColumn](https://docs.liquibase.com/change-types/drop-column.html)."""

    dropColumn: DropColumnAttributes


class DropFunctionAttributes(TypedDict):
    """Permitted attributes for `DropFunction.dropFunction`."""

    catalogName: Optional[str]
    functionName: str
    schemaName: Optional[str]


class DropFunction(TypedDict):
    """Permitted attributes for change
    [dropFunction](https://docs.liquibase.com/change-types/drop-function.html)."""

    dropFunction: DropFunctionAttributes


class DropIndexAttributes(TypedDict):
    """Permitted attributes for `DropIndex.dropIndex`."""

    catalogName: Optional[str]
    indexName: str
    schemaName: Optional[str]
    tableName: str


class DropIndex(TypedDict):
    """Permitted attributes for change
    [dropIndex](https://docs.liquibase.com/change-types/drop-index.html)."""

    dropIndex: DropIndexAttributes


class DropPackageAttributes(TypedDict):
    """Permitted attributes for `DropPackage.DropPackage`."""

    catalogName: Optional[str]
    packageName: str
    schemaName: Optional[str]


class DropPackage(TypedDict):
    """Permitted attributes for change
    [dropPackage](https://docs.liquibase.com/change-types/drop-package.html)."""

    dropPackage: DropPackageAttributes


class DropPackageBodyAttributes(TypedDict):
    """Permitted attributes for `DropPackageBody.dropPackageBody`."""

    catalogName: Optional[str]
    packageBodyName: str
    schemaName: Optional[str]


class DropPackageBody(TypedDict):
    """Permitted attributes for change
    [dropPackageBody](https://docs.liquibase.com/change-types/drop-package-body.html).
    """

    dropPackageBody: DropPackageBodyAttributes


class DropProcedureAttributes(TypedDict):
    """Permitted attributes for `DropProcedure.dropProcedure`."""

    catalogName: Optional[str]
    procedureName: str
    schemaName: Optional[str]


class DropProcedure(TypedDict):
    """Permitted attributes for change
    [dropProcedure](https://docs.liquibase.com/change-types/drop-procedure.html).
    """

    dropProcedure: DropProcedureAttributes


class DropSequenceAttributes(TypedDict):
    """Permitted attributes for `DropSequence.dropSequence`."""

    catalogName: Optional[str]
    schemaName: Optional[str]
    sequenceName: str


class DropSequence(TypedDict):
    """Permitted attributes for change
    [dropSequence](https://docs.liquibase.com/change-types/drop-sequence.html).
    """

    dropSequence: DropSequenceAttributes


class DropSynonymAttributes(TypedDict):
    """Permitted attributes for `DropSynonym.dropSynonym`."""

    objectType: Optional[str]
    private: Optional[bool]
    synonymCatalogName: Optional[str]
    synonymName: str
    synonymSchemaName: Optional[str]


class DropSynonym(TypedDict):
    """Permitted attributes for change
    [DropSynonym](https://docs.liquibase.com/change-types/drop-synonym.html).
    """

    DropSynonym: DropSynonymAttributes


class DropTableAttributes(TypedDict):
    """Permitted attributes for `DropTable.dropSequence`."""

    cascadeConstraints: Optional[bool]
    catalogName: Optional[str]
    schemaName: Optional[str]
    tableName: str


class DropTable(TypedDict):
    """Permitted attributes for change
    [dropTable](https://docs.liquibase.com/change-types/drop-table.html).
    """

    dropTable: DropTableAttributes


class DropTriggerAttributes(TypedDict):
    """Permitted attributes for `DropTrigger.dropTrigger`."""

    catalogName: Optional[str]
    schemaName: Optional[str]
    scope: Optional[str]
    tableName: Optional[str]
    triggerName: str


class DropTrigger(TypedDict):
    """Permitted attributes for change
    [dropTrigger](https://docs.liquibase.com/change-types/drop-trigger.html).
    """

    dropTrigger: DropTriggerAttributes


class DropViewAttributes:
    """Permitted attributes for `DropView.dropView`."""

    catalogName: Optional[str]
    ifExists: Optional[bool]
    schemaName: Optional[str]
    viewName: str


class DropView:
    """Permitted attributes for change
    [dropView](https://docs.liquibase.com/change-types/drop-view.html).
    """

    dropView: DropViewAttributes


class EnableTriggerAttributes:
    """Permitted attributes for `EnableTrigger.enableTrigger`."""

    catalogName: Optional[str]
    schemaName: Optional[str]
    scope: Optional[str]
    tableName: Optional[str]
    triggerName: str


class EnableTrigger:
    """Permitted attributes for change
    [enableTrigger](https://docs.liquibase.com/change-types/enable-trigger.html).
    """

    enableTrigger: EnableTriggerAttributes
