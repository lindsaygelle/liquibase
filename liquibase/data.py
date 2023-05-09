# pylint: disable=C0103,R,C0114
from typing import List, Literal, Optional, TypedDict

from liquibase import entity


class LookupTable(TypedDict):
    """Permitted attributes for `AddLookupTable.addLookupTable`."""

    constraintName: Optional[str]
    existingColumnName: str
    existingTableCatalogName: Optional[str]
    existingTableName: str
    existingTableSchemaName: Optional[str]
    newColumnDataType: str
    newColumnName: str
    newTableCatalogName: Optional[str]
    newTableName: str
    newTableSchemaName: Optional[str]


class AddLookupTable(TypedDict):
    """Permitted attributes for change
    [addLookupTable](https://docs.liquibase.com/change-types/add-lookup-table.html).
    """

    addLookupTable: LookupTable


class Param(TypedDict):
    """Permitted attributes for `WhereParam.param`."""

    name: str
    value: Optional[str]
    valueNumeric: Optional[int]
    valueBoolean: Optional[bool]
    valueDate: Optional[str]
    valueComputed: Optional[str]
    valueSequenceNext: Optional[str]
    valueSequenceCurrent: Optional[str]


class WhereParam(TypedDict):
    """Permitted attributes for `Delete.delete`, `Update.update`."""

    param: Param


class DeleteAttributes(TypedDict):
    """Permitted attributes for `AddDelete.delete`."""

    catalogName: Optional[str]
    schemaName: Optional[str]
    tableName: str
    where: Optional[str]
    whereParams: Optional[List[WhereParam]]


class Delete(TypedDict):
    """Permitted attributes for change
    [delete](https://docs.liquibase.com/change-types/delete.html).
    """

    delete: DeleteAttributes


class InsertAttributes(TypedDict):
    """Permitted attributes for `Insert.insert`."""

    catalogName: Optional[str]
    columns: List[entity.Column]
    dbms: Optional[str]
    schemaName: Optional[str]
    tableName: str


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


class ColumnAttributes(TypedDict):
    """Permitted attributes for `Colum.column`."""

    header: Optional[str]
    index: int
    name: str
    type: ColumnType


class Column(TypedDict):
    """Permitted attributes for `[LoadDataAttributes | LoadUpdateDataAttributes].columns[*]`."""

    column: ColumnAttributes


class LoadAttributes(TypedDict):
    """Common attributes for `LoadDataAttributes`, `LoadUpdateDataAttributes`."""

    catalogName: Optional[str]
    columns: List[Column]
    commentLineStartsWith: Optional[str]
    encoding: Optional[str]
    file: str
    quotchar: Optional[str]
    relativeToChangelogFile: Optional[bool]
    schemaName: Optional[str]
    separator: Optional[str]
    tableName: str
    usePreparedStatements: Optional[bool]


class LoadDataAttributes(LoadAttributes):
    """Permitted attributes for `LoadData.loadData`."""

    onlyUpdate: bool
    primaryKey: bool


class LoadData(TypedDict):
    """Permitted attributes for change
    [loadData](https://docs.liquibase.com/change-types/load-data.html).
    """

    loadData: LoadDataAttributes


class LoadUpdateDataAttributes(LoadAttributes):
    """Permitted attributes for `LoadUpdateData.loadUpdateData`."""


class LoadUpdateData(TypedDict):
    """Permitted attributes for change
    [loadUpdateData](https://docs.liquibase.com/change-types/load-update-data.html).
    """

    loadUpdateData: LoadUpdateDataAttributes


class MergeColumn(TypedDict):
    """Permitted attributes for `MergeColumns.mergeColumns`."""

    catalogName: Optional[str]
    column1Name: str
    column2Name: str
    finalColumnName: str
    finalColumnType: str
    joinString: Optional[str]
    schemaName: Optional[str]
    tableName: str


class MergeColumns(TypedDict):
    """Permitted attributes for change
    [mergeColumns](https://docs.liquibase.com/change-types/merge-columns.html).
    """

    mergeColumns: MergeColumn


class ModifyData(TypedDict):
    """Permitted attributes for `ModifyDataType.modifyDataType`."""

    catalogName: Optional[str]
    columnName: str
    newDataType: str
    schemaName: Optional[str]
    tableName: str


class ModifyDataType(TypedDict):
    """Permitted attributes for change
    [modifyDataType](https://docs.liquibase.com/change-types/modify-data-type.html).
    """

    modifyDataType: ModifyData


class UpdateAttributes(TypedDict):
    """Permitted attributes for `Update.update`."""

    catalogName: Optional[str]
    columns: List[entity.Column]
    schemaName: Optional[str]
    tableName: str
    where: Optional[str]
    whereParam: Optional[WhereParam]


class Update(TypedDict):
    """Permitted attributes for change
    [update](https://docs.liquibase.com/change-types/update.html).
    """

    update: UpdateAttributes
