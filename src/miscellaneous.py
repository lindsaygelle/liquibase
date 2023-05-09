# pylint: disable=C0103,R,C0114
from dataclasses import dataclass
from typing import Any, Dict, List, Literal, Optional, TypedDict


@dataclass
class CustomChange(TypedDict):
    """Permitted attributes for change
    [customChange](https://docs.liquibase.com/change-types/custom-change.html).
    """

    customChange: Dict[str, Any]


@dataclass
class Empty(TypedDict):
    """Permitted attributes for change
    [empty](https://docs.liquibase.com/change-types/empty.html).
    """

    empty: Dict[Any, Any]


@dataclass
class Arg(TypedDict):
    """Permitted attributes for `ExecuteCommandAttributes.args[*]`."""

    value: str


@dataclass
class ExecuteCommandAttributes(TypedDict):
    """Permitted attributes for `ExecuteCommand.executeCommand`."""

    args: List[Arg]
    executable: str
    os: str
    timeout: str


@dataclass
class ExecuteCommand(TypedDict):
    """Permitted attributes for change
    [executeCommand](https://docs.liquibase.com/change-types/execute-command.html).
    """

    executeCommand: ExecuteCommandAttributes


@dataclass
class IncludeAttributes(TypedDict):
    """Permitted attributes for `Include.include`."""

    file: str
    relativeToChangelogFile: bool
    context: str
    labels: str


@dataclass
class Include(TypedDict):
    """Permitted attributes for change
    [include](https://docs.liquibase.com/change-types/include.html).
    """

    include: IncludeAttributes


@dataclass
class IncludeAllAttributes(TypedDict):
    """Permitted attributes for `IncludeAll.includeAll`."""

    context: str
    errorIfMissingOrEmpty: bool
    filter: str
    path: str
    relativeToChangelogFile: bool
    resourceComparator: str


@dataclass
class IncludeAll(TypedDict):
    """Permitted attributes for change
    [includeAll](https://docs.liquibase.com/change-types/includeall.html).
    """

    includeAll: IncludeAllAttributes


@dataclass
class MarkUnusedAttributes(TypedDict):
    """Permitted attributes for `MarkUnused.markUnused`."""

    catalogName: str
    columnName: str
    schemaName: str
    tableName: str


@dataclass
class MarkUnused(TypedDict):
    """Permitted attributes for change
    [markUnused](https://docs.liquibase.com/change-types/mark-unused.html).
    """

    markUnused: MarkUnusedAttributes


RunWith = Literal["jdbc", "psql", "sqlplus", "sqlcmd", "custom"]


@dataclass
class ModifyChangeSet(TypedDict):
    """Permitted attributes for `ModifyChangeSets.modifyChangeSets`."""

    include: Optional[Include]
    includeAll: Optional[IncludeAll]
    runWith: RunWith


@dataclass
class ModifyChangeSets(TypedDict):
    """Permitted attributes for change
    [modifyChangeSets](https://docs.liquibase.com/change-types/modifychangesets.html).
    """

    modifyChangeSets: ModifyChangeSet


@dataclass
class OutputAttributes(TypedDict):
    """Permitted attributes for `Output.output`."""

    message: str
    target: str


@dataclass
class Output(TypedDict):
    """Permitted attributes for change
    [output](https://docs.liquibase.com/change-types/output.html).
    """

    output: OutputAttributes


@dataclass
class SqlAttributes(TypedDict):
    """Permitted attributes for `Sql.sql`."""

    dbms: str
    endDelimiter: str
    splitStatements: bool
    sql: str
    stripComments: bool
    comment: str


@dataclass
class Sql(TypedDict):
    """Permitted attributes for change
    [sql](https://docs.liquibase.com/change-types/sql.html).
    """

    sql: SqlAttributes


@dataclass
class SqlFileAttributes(TypedDict):
    """Permitted attributes for `SqlFile.sqlFile`."""

    dbms: str
    encoding: str
    endDelimiter: str
    path: str
    relativeToChangelogFile: bool
    splitStatements: bool
    stripComments: bool


@dataclass
class SqlFile(TypedDict):
    """Permitted attributes for change
    [sqlFile](https://docs.liquibase.com/change-types/sql-file.html).
    """

    sqlFile: SqlFileAttributes
