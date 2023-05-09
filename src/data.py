# pylint: disable=C0103,R,C0114
from dataclasses import dataclass
from typing import List, Literal, TypedDict

# pylint: disable=E0401
import entity


@dataclass
class LookupTable(TypedDict):
    """Permitted attributes for `AddLookupTable.addLookupTable`."""

    constraintName: str
    existingColumnName: str
    existingTableName: str
    newColumnDataType: str
    newColumnName: str
    newTableCatalogName: str
    newTableName: str
    newTableSchemaName: str


@dataclass
class AddLookupTable(TypedDict):
    """Permitted attributes for change
    [addLookupTable](https://docs.liquibase.com/change-types/add-lookup-table.html).
    """

    addLookupTable: LookupTable


@dataclass
class Param(TypedDict):
    """Permitted attributes for `WhereParam.param`."""

    name: str
    value: str
    valueNumeric: int
    valueBoolean: bool
    valueDate: str
    valueComputed: str
    valueSequenceNext: str
    valueSequenceCurrent: str


@dataclass
class WhereParam(TypedDict):
    """Permitted attributes for `Delete.delete`, `Update.update`."""

    param: Param


@dataclass
class DeleteAttributes(TypedDict):
    """Permitted attributes for `AddDelete.delete`."""

    catalogName: str
    schemaName: str
    tableName: str
    where: str
    whereParams: List[WhereParam]


@dataclass
class Delete(TypedDict):
    """Permitted attributes for change
    [delete](https://docs.liquibase.com/change-types/delete.html).
    """

    delete: DeleteAttributes


@dataclass
class InsertAttributes(TypedDict):
    """Permitted attributes for `Insert.insert`."""

    catalogName: str
    columns: List[entity.Column]
    dbms: str
    schemaName: str
    tableName: str


@dataclass
class Insert(TypedDict):
    """Permitted attributes for change
    [insert](https://docs.liquibase.com/change-types/insert.html).
    """

    insert: InsertAttributes


ColumnType = Literal[
    "BLOB",
    "BOOLEAN",
    "CLOB",
    "COMPUTED",
    "DATE",
    "NUMERIC",
    "OTHER",
    "SEQUENCE",
    "SKIP",
    "STRING",
    "UNKNOWN",
    "UUID",
]


@dataclass
class ColumnAttributes(TypedDict):
    """Permitted attributes for `Colum.column`."""

    header: str
    index: int
    name: str
    type: ColumnType


@dataclass
class Column(TypedDict):
    """Permitted attributes for `[LoadDataAttributes | LoadUpdateDataAttributes].columns[*]`."""

    column: ColumnAttributes


@dataclass
class LoadAttributes(TypedDict):
    """Common attributes for `LoadDataAttributes`, `LoadUpdateDataAttributes`."""

    catalogName: str
    columns: List[Column]
    commentLineStartsWith: str
    encoding: str
    file: str
    quotchar: str
    relativeToChangelogFile: bool
    schemaName: str
    separator: str
    tableName: str
    usePreparedStatements: bool


@dataclass
class LoadDataAttributes(LoadAttributes):
    """Permitted attributes for `LoadData.loadData`."""

    onlyUpdate: bool
    primaryKey: bool


@dataclass
class LoadData(TypedDict):
    """Permitted attributes for change
    [loadData](https://docs.liquibase.com/change-types/load-data.html).
    """

    loadData: LoadDataAttributes


@dataclass
class LoadUpdateDataAttributes(LoadAttributes):
    """Permitted attributes for `LoadUpdateData.loadUpdateData`."""


@dataclass
class LoadUpdateData(TypedDict):
    """Permitted attributes for change
    [loadUpdateData](https://docs.liquibase.com/change-types/load-update-data.html).
    """

    loadUpdateData: LoadUpdateDataAttributes


@dataclass
class MergeColumn(TypedDict):
    """Permitted attributes for `MergeColumns.mergeColumns`."""

    catalogName: str
    column1Name: str
    column2Name: str
    finalColumnName: str
    finalColumnType: str
    joinString: str
    schemaName: str
    tableName: str


@dataclass
class MergeColumns(TypedDict):
    """Permitted attributes for change
    [mergeColumns](https://docs.liquibase.com/change-types/merge-columns.html).
    """

    mergeColumns: MergeColumn


@dataclass
class ModifyData(TypedDict):
    """Permitted attributes for `ModifyDataType.modifyDataType`."""

    catalogName: str
    columnName: str
    newDataType: str
    schemaName: str
    tableName: str


@dataclass
class ModifyDataType(TypedDict):
    """Permitted attributes for change
    [modifyDataType](https://docs.liquibase.com/change-types/modify-data-type.html).
    """

    modifyDataType: ModifyData


@dataclass
class UpdateAttributes(TypedDict):
    """Permitted attributes for `Update.update`."""

    catalogName: str
    columns: List[entity.Column]
    schemaName: str
    tableName: str
    where: str
    whereParam: WhereParam


@dataclass
class Update(TypedDict):
    """Permitted attributes for change
    [update](https://docs.liquibase.com/change-types/update.html).
    """

    update: UpdateAttributes
