# pylint: disable=C0103,R,C0114
from typing import Any, Dict, List, Literal, Optional, TypedDict


class CustomChange(TypedDict):
    """Permitted attributes for change
    [customChange](https://docs.liquibase.com/change-types/custom-change.html).
    """

    customChange: Dict[str, Dict[str, Dict[str, Any]]]


class Empty(TypedDict):
    """Permitted attributes for change
    [empty](https://docs.liquibase.com/change-types/empty.html).
    """

    empty: Dict[str, Dict[str, Dict[str, Any]]]


class Arg(TypedDict):
    """Permitted attributes for `ExecuteCommandAttributes.args[*]`."""

    value: str


class ExecuteCommandAttributes(TypedDict):
    """Permitted attributes for `ExecuteCommand.executeCommand`."""

    args: Optional[List[Arg]]
    executable: str
    os: Optional[str]
    timeout: Optional[str]


class ExecuteCommand(TypedDict):
    """Permitted attributes for change
    [executeCommand](https://docs.liquibase.com/change-types/execute-command.html).
    """

    executeCommand: ExecuteCommandAttributes


class IncludeAttributes(TypedDict):
    """Permitted attributes for `Include.include`."""

    file: str
    relativeToChangelogFile: Optional[bool]
    context: Optional[str]
    labels: Optional[str]


class Include(TypedDict):
    """Permitted attributes for change
    [include](https://docs.liquibase.com/change-types/include.html).
    """

    include: IncludeAttributes


class IncludeAllAttributes(TypedDict):
    """Permitted attributes for `IncludeAll.includeAll`."""

    context: Optional[str]
    errorIfMissingOrEmpty: Optional[bool]
    filter: Optional[str]
    path: str
    relativeToChangelogFile: Optional[bool]
    resourceComparator: Optional[str]


class IncludeAll(TypedDict):
    """Permitted attributes for change
    [includeAll](https://docs.liquibase.com/change-types/includeall.html).
    """

    includeAll: IncludeAllAttributes


class MarkUnusedAttributes(TypedDict):
    """Permitted attributes for `MarkUnused.markUnused`."""

    catalogName: Optional[str]
    columnName: str
    schemaName: Optional[str]
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
    target: Optional[str]


class Output(TypedDict):
    """Permitted attributes for change
    [output](https://docs.liquibase.com/change-types/output.html).
    """

    output: OutputAttributes


class SqlAttributes(TypedDict):
    """Permitted attributes for `Sql.sql`."""

    dbms: Optional[str]
    endDelimiter: Optional[str]
    splitStatements: Optional[str]
    sql: str
    stripComments: Optional[bool]


class Sql(TypedDict):
    """Permitted attributes for change
    [sql](https://docs.liquibase.com/change-types/sql.html).
    """

    sql: SqlAttributes


class SqlFileAttributes(TypedDict):
    """Permitted attributes for `SqlFile.sqlFile`."""

    dbms: Optional[str]
    encoding: Optional[str]
    endDelimiter: Optional[str]
    path: str
    relativeToChangelogFile: Optional[bool]
    splitStatements: Optional[bool]
    stripComments: Optional[bool]


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
