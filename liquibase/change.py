# pylint: disable=C0103,R,C0114
from typing import Any, Dict, List, Literal, Optional, TypedDict, Union

from liquibase import constraint
from liquibase import data
from liquibase import entity
from liquibase import miscellaneous
from liquibase import precondition

ChangeConstraint = Union[
    constraint.AddCheckConstraint,
    constraint.AddForeignKeyConstraint,
    constraint.AddNotNullConstraint,
    constraint.AddPrimaryKey,
    constraint.AddUniqueConstraint,
]

ChangeData = Union[
    data.AddLookupTable,
    data.Delete,
    data.Insert,
    data.LoadData,
    data.LoadUpdateData,
    data.MergeColumns,
    data.ModifyDataType,
    data.Update,
]


ChangeEntity = Union[
    entity.AddAutoIncrement,
    entity.AddColumn,
    entity.AlterSequence,
    entity.CreateFunction,
    entity.CreateIndex,
    entity.CreatePackage,
    entity.CreatePackageBody,
    entity.CreateProcedure,
    entity.CreateSequence,
    entity.CreateSynonym,
    entity.CreateTable,
    entity.CreateTrigger,
    entity.CreateView,
]

Changes = Union[ChangeConstraint, ChangeData, ChangeEntity]

ObjectQuotingStrategy = Literal[
    "LEGACY", "QUOTE_ALL_OBJECTS", "QUOTE_ONLY_RESERVED_WORDS"
]

Rollback = Dict[str, Dict[str, Dict[str, Any]]]

RunOrder = Literal["first", "last"]


class ChangeSetAttributes(TypedDict):
    """Permitted attributes for `ChangeSet.changeSet`."""

    author: str
    changes: List[Changes]
    comment: Optional[str]
    contextFilter: Optional[str]
    created: Optional[str]
    dbms: Optional[str]
    id: str
    failOnError: Optional[bool]
    ignore: Optional[bool]
    labels: Optional[str]
    logicalFilePath: Optional[str]
    objectQuotingStrategy: Optional[ObjectQuotingStrategy]
    preConditions: List[precondition.PreCondition]
    rollback: Optional[Rollback]
    runAlways: Optional[bool]
    runInTransaction: Optional[bool]
    runOnChange: Optional[bool]
    runOrder: Optional[RunOrder]
    runWith: Optional[miscellaneous.RunWith]
    validCheckSum: Optional[str]


class ChangeSet(TypedDict):
    """Permitted attributes for
    [changeSet](https://docs.liquibase.com/concepts/changelogs/changeset.html).
    """

    changeSet: ChangeSetAttributes


class Property(TypedDict):
    """Permitted attributes for `ChangeLog.property`."""

    dbms: Optional[str]
    context: Optional[str]
    file: Optional[str]
    name: str
    relativeToChangelogFile: Optional[bool]
    value: str


ChangeLog = Union[
    ChangeSet,
    precondition.PreConditions,
    Property,
    miscellaneous.Include,
    miscellaneous.IncludeAll,
    miscellaneous.ModifyChangeSets,
]


class DatabaseChangeLog(TypedDict):
    """Permitted attributes for
    [databaseChangeLog](https://docs.liquibase.com/concepts/changelogs/home.html).
    """

    databaseChangeLog: List[ChangeLog]
