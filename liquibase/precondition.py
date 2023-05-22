# pylint: disable=C0103,R,C0114
from typing import Any, List, Literal, Optional, TypedDict


class ColumnExistsAttributes(TypedDict):
    """Permitted attributes for `ColumnExists.columnExists`."""

    columnName: str
    schemaName: Optional[str]
    tableName: str


class ColumnExists(TypedDict):
    """Permitted attributes for
    [columnExists](https://docs.liquibase.com/concepts/changelogs/preconditions.html).
    """

    columnExists: ColumnExistsAttributes


class ChangeLogPropertyDefinedAttributes(TypedDict):
    """Permitted attributes for `ChangeLogPropertyDefined.changeLogPropertyDefined`."""

    property: str
    value: Optional[str]


class ChangeLogPropertyDefined(TypedDict):
    """Permitted attributes for
    [changeLogPropertyDefined](https://docs.liquibase.com/concepts/changelogs/preconditions.html).
    """

    changeLogPropertyDefined: ChangeLogPropertyDefinedAttributes


class ChangeSetExecutedAttributes(TypedDict):
    """Permitted attributes for `ChangeSetExecutedAttributes.changeSetExecuted`."""

    author: str
    changelogFile: str
    id: str


class ChangeSetExecuted(TypedDict):
    """Permitted attributes for
    [changeSetExecuted](https://docs.liquibase.com/concepts/changelogs/preconditions.html).
    """

    changeSetExecuted: ChangeSetExecutedAttributes


class CustomPreconditionParam(TypedDict):
    """Permitted attributes for `CustomPreconditionAttributes.param[*]`."""

    name: str
    value: Any


class CustomPreconditionAttributes(TypedDict):
    """Permitted attributes for `CustomPrecondition.customPrecondition`."""

    className: str
    param: List[CustomPreconditionParam]


class CustomPrecondition(TypedDict):
    """Permitted attributes for
    [customPrecondition](https://docs.liquibase.com/concepts/changelogs/preconditions.html).
    """

    customPrecondition: CustomPreconditionAttributes


class DbmsAttributes(TypedDict):
    """Permitted attributes for `Dbms.dbms`."""

    type: str


class Dbms(TypedDict):
    """Permitted attributes for
    [dbms](https://docs.liquibase.com/concepts/changelogs/preconditions.html).
    """

    dbms: DbmsAttributes


class SqlCheckAttributes(TypedDict):
    """Permitted attributes for `SqlCheck.sqlCheck`."""

    expectedResult: str
    query: str


class SqlCheck(TypedDict):
    """Permitted attributes for
    [sqlCheck](https://docs.liquibase.com/concepts/changelogs/preconditions.html).
    """

    sqlCheck: SqlCheckAttributes


class RowCountAttributes(TypedDict):
    """Permitted attributes for `RowCount.rowCount`."""

    expectedRows: int
    tableName: str


class RowCount(TypedDict):
    """Permitted attributes for
    [rowCount](https://docs.liquibase.com/concepts/changelogs/preconditions.html).
    """

    rowCount: RowCountAttributes


class RunningAsAttributes(TypedDict):
    """Permitted attributes for `RunningAs.runningAs`."""

    columnName: str
    schemaName: Optional[str]
    tableName: str


class RunningAs(TypedDict):
    """Permitted attributes for
    [runningAs](https://docs.liquibase.com/concepts/changelogs/preconditions.html).
    """

    runningAs: RunningAsAttributes


class ForeignKeyConstraintExistsAttributes(TypedDict):
    """Permitted attributes for `ForeignKeyConstraintExists.foreignKeyConstraintExists`."""

    foreignKeyName: str
    foreignKeyTableName: str
    schemaName: Optional[str]


class ForeignKeyConstraintExists(TypedDict):
    """Permitted attributes for
    [foreignKeyConstraintExists](https://docs.liquibase.com/concepts/changelogs/preconditions.html).
    """

    foreignKeyConstraintExists: ForeignKeyConstraintExistsAttributes


class IndexExistsAttributes(TypedDict):
    """Permitted attributes for `IndexExists.indexExists`."""

    columnNames: Optional[str]
    indexName: Optional[str]
    schemaName: Optional[str]
    tableName: Optional[str]


class IndexExists(TypedDict):
    """Permitted attributes for
    [indexExists](https://docs.liquibase.com/concepts/changelogs/preconditions.html).
    """

    indexExists: IndexExistsAttributes


class PrimaryKeyExistsAttributes(TypedDict):
    """Permitted attributes for `PrimaryKeyExists.PrimaryKeyExists`."""

    primaryKeyName: str
    schemaName: Optional[str]
    tableName: Optional[str]


class PrimaryKeyExists(TypedDict):
    """Permitted attributes for
    [primaryKeyExists](https://docs.liquibase.com/concepts/changelogs/preconditions.html).
    """

    primaryKeyExists: PrimaryKeyExistsAttributes


class SequenceExistsAttributes(TypedDict):
    """Permitted attributes for `SequenceExists.sequenceExists`."""

    schemaName: Optional[str]
    sequenceName: str


class SequenceExists(TypedDict):
    """Permitted attributes for
    [sequenceExists](https://docs.liquibase.com/concepts/changelogs/preconditions.html).
    """

    sequenceExists: SequenceExistsAttributes


class TableExistsAttributes(TypedDict):
    """Permitted attributes for `TableExists.tableExists`."""

    schemaName: Optional[str]
    tableName: str


class TableExists(TypedDict):
    """Permitted attributes for
    [tableExists](https://docs.liquibase.com/concepts/changelogs/preconditions.html).
    """

    tableExists: TableExistsAttributes


class UniqueConstraintExistsAttributes(TypedDict):
    """Permitted attributes for `UniqueConstraintExists.uniqueConstraintExists`."""

    columnNames: Optional[str]
    constraintName: str
    tableName: str


class UniqueConstraintExists(TypedDict):
    """Permitted attributes for
    [uniqueConstraintExists](https://docs.liquibase.com/concepts/changelogs/preconditions.html).
    """

    uniqueConstraintExists: UniqueConstraintExistsAttributes


class ViewExistsAttributes(TypedDict):
    """Permitted attributes for `ViewExists.viewExists`."""

    schemaName: Optional[str]
    viewName: str


class ViewExists(TypedDict):
    """Permitted attributes for
    [viewExists](https://docs.liquibase.com/concepts/changelogs/preconditions.html).
    """

    viewExists: ViewExistsAttributes


OnError = Literal["CONTINUE", "HALT", "MARK_RAN", "WARN"]
OnFail = OnError
OnSqlOutput = Literal["FAIL", "IGNORE", "TEST"]
OnSqlUpdate = OnSqlOutput


class PreCondition(TypedDict):
    """Permitted attributes for `PreConditions.preCondition[*]`."""

    changeLogPropertyDefined: Optional[ChangeLogPropertyDefinedAttributes]
    changeSetExecuted: Optional[ChangeSetExecutedAttributes]
    columnExists: Optional[ColumnExistsAttributes]
    customPrecondition: Optional[CustomPreconditionAttributes]
    dbms: Optional[DbmsAttributes]
    foreignKeyConstraintExists: Optional[ForeignKeyConstraintExistsAttributes]
    indexExists: Optional[IndexExistsAttributes]
    primaryKeyExists: Optional[PrimaryKeyExistsAttributes]
    onError: Optional[OnError]
    onErrorMessage: Optional[str]
    onFail: Optional[OnFail]
    onFailMessage: Optional[str]
    onSqlOutput: Optional[OnSqlOutput]
    onUpdateSql: Optional[OnSqlUpdate]
    sequenceExists: Optional[SequenceExistsAttributes]
    sqlCheck: Optional[SqlCheckAttributes]
    tableExists: Optional[TableExistsAttributes]
    rowCount: Optional[RowCountAttributes]
    runningAs: Optional[RunningAsAttributes]
    uniqueConstraintExists: Optional[UniqueConstraintExistsAttributes]
    viewExists: Optional[ViewExistsAttributes]


class PreConditions(TypedDict):
    """Permitted attributes for
    [preConditions](https://docs.liquibase.com/concepts/changelogs/preconditions.html).
    """

    preConditions: List[PreCondition]
