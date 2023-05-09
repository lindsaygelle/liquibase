# pylint: disable=C0103,R,C0114
from typing import Any, Dict, List, Literal, Optional, TypedDict


class CustomChange(TypedDict):
    """Permitted attributes for change
    [customChange](https://docs.liquibase.com/change-types/custom-change.html).
    """

    customChange: Dict[str, Any]


class Empty(TypedDict):
    """Permitted attributes for change
    [empty](https://docs.liquibase.com/change-types/empty.html).
    """

    empty: Dict[Any, Any]


class Arg(TypedDict):
    """Permitted attributes for `ExecuteCommandAttributes.args[*]`."""

    value: str


class ExecuteCommandAttributes(TypedDict):
    """Permitted attributes for `ExecuteCommand.executeCommand`."""

    args: List[Arg]
    executable: str
    os: str
    timeout: str


class ExecuteCommand(TypedDict):
    """Permitted attributes for change
    [executeCommand](https://docs.liquibase.com/change-types/execute-command.html).
    """

    executeCommand: ExecuteCommandAttributes


class IncludeAttributes(TypedDict):
    """Permitted attributes for `Include.include`."""

    file: str
    relativeToChangelogFile: bool
    context: str
    labels: str


class Include(TypedDict):
    """Permitted attributes for change
    [include](https://docs.liquibase.com/change-types/include.html).
    """

    include: IncludeAttributes


class IncludeAllAttributes(TypedDict):
    """Permitted attributes for `IncludeAll.includeAll`."""

    context: str
    errorIfMissingOrEmpty: bool
    filter: str
    path: str
    relativeToChangelogFile: bool
    resourceComparator: str


class IncludeAll(TypedDict):
    """Permitted attributes for change
    [includeAll](https://docs.liquibase.com/change-types/includeall.html).
    """

    includeAll: IncludeAllAttributes


class MarkUnusedAttributes(TypedDict):
    """Permitted attributes for `MarkUnused.markUnused`."""

    catalogName: str
    columnName: str
    schemaName: str
    tableName: str


class MarkUnused(TypedDict):
    """Permitted attributes for change
    [markUnused](https://docs.liquibase.com/change-types/mark-unused.html).
    """

    markUnused: MarkUnusedAttributes


RunWith = Literal["jdbc", "psql", "sqlplus", "sqlcmd", "custom"]


class ModifyChangeSet(TypedDict):
    """Permitted attributes for `ModifyChangeSets.modifyChangeSets`."""

    include: Optional[Include]
    includeAll: Optional[IncludeAll]
    runWith: RunWith


class ModifyChangeSets(TypedDict):
    """Permitted attributes for change
    [modifyChangeSets](https://docs.liquibase.com/change-types/modifychangesets.html).
    """

    modifyChangeSets: ModifyChangeSet


class OutputAttributes(TypedDict):
    """Permitted attributes for `Output.output`."""

    message: str
    target: str


class Output(TypedDict):
    """Permitted attributes for change
    [output](https://docs.liquibase.com/change-types/output.html).
    """

    output: OutputAttributes


class SqlAttributes(TypedDict):
    """Permitted attributes for `Sql.sql`."""

    dbms: str
    endDelimiter: str
    splitStatements: bool
    sql: str
    stripComments: bool
    comment: str


class Sql(TypedDict):
    """Permitted attributes for change
    [sql](https://docs.liquibase.com/change-types/sql.html).
    """

    sql: SqlAttributes


class SqlFileAttributes(TypedDict):
    """Permitted attributes for `SqlFile.sqlFile`."""

    dbms: str
    encoding: str
    endDelimiter: str
    path: str
    relativeToChangelogFile: bool
    splitStatements: bool
    stripComments: bool


class SqlFile(TypedDict):
    """Permitted attributes for change
    [sqlFile](https://docs.liquibase.com/change-types/sql-file.html).
    """

    sqlFile: SqlFileAttributes


class StopAttributes(TypedDict):
    """Permitted attributes for `Stop.stop`."""

    message: str


class Stop(TypedDict):
    """Permitted attributes for change
    [stop](https://docs.liquibase.com/change-types/stop.html).
    """

    stop: StopAttributes


class TagDatabaseAttributes(TypedDict):
    """Permitted attributes for `TagDatabase.tag`."""

    tag: str


class TagDatabase(TypedDict):
    """Permitted attributes for change
    [tagDatabase](https://docs.liquibase.com/change-types/tag-database.html).
    """

    tagDatabase: TagDatabaseAttributes
