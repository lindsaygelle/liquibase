# pylint: disable=C0103,R,C0114
from typing import Any, Dict, List, Literal, Optional, TypedDict, Union

# pylint: disable=E0401
import constraint
import entity
import miscellaneous

ChangeConstraint = Union[
    constraint.AddCheckConstraint,
    constraint.AddForeignKeyConstraint,
    constraint.AddNotNullConstraint,
    constraint.AddPrimaryKey,
    constraint.AddUniqueConstraint,
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

ChangeMiscellaneous = Union[
    miscellaneous.AddLookupTable,
    miscellaneous.Delete,
    miscellaneous.Insert,
    miscellaneous.LoadData,
    miscellaneous.LoadUpdateData,
    miscellaneous.MergeColumns,
    miscellaneous.ModifyDataType,
    miscellaneous.Update,
]


Changes = Union[ChangeConstraint, ChangeEntity, ChangeMiscellaneous]

PreCondition = Dict[str, Dict[str, Dict[str, Any]]]

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
    preConditions: List[PreCondition]
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


class ChangeLog(TypedDict):
    """Permitted attributes for `DatabaseChangeLog.databaseChangeLog[*]`."""

    changeSet: Optional[ChangeSet]
    preConditions: Optional[List[PreCondition]]
    property: Optional[Property]
    include: Optional[miscellaneous.Include]
    includeAll: Optional[miscellaneous.IncludeAll]
    modifyChangeSets: Optional[List[miscellaneous.ModifyChangeSets]]


class DatabaseChangeLog(TypedDict):
    """Permitted attributes for
    [databaseChangeLog](https://docs.liquibase.com/concepts/changelogs/home.html).
    """

    databaseChangeLog: List[ChangeLog]
