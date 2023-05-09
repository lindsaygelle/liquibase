# pylint: disable=C0103,R,C0114
from typing import List, TypedDict
from . import entity


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


class AddLookupTable(TypedDict):
    """Permitted attributes for change
    [addLookupTable](https://docs.liquibase.com/change-types/add-lookup-table.html).
    """

    addLookupTable: LookupTable


class Param(TypedDict):
    """Permitted attributes for `[DeleteParam].param`."""

    name: str
    value: str
    valueNumeric: int
    valueBoolean: bool
    valueDate: str
    valueComputed: str
    valueSequenceNext: str
    valueSequenceCurrent: str


class DeleteParam(TypedDict):
    """Permitted attributes for change
    [delete](https://docs.liquibase.com/change-types/delete.html).
    """

    param: Param


class DeleteAttributes(TypedDict):
    """Permitted attributes for `AddDelete.delete`."""

    catalogName: str
    schemaName: str
    tableName: str
    where: str
    whereParams: List[DeleteParam]


class Delete(TypedDict):
    """Permitted attributes for change
    [delete](https://docs.liquibase.com/change-types/delete.html).
    """

    delete: DeleteAttributes


class InsertAttributes(TypedDict):
    """Permitted attributes for `Insert.insert`."""

    catalogName: str
    columns: List[entity.Column]
    dbms: str
    schemaName: str
    tableName: str


class Insert(TypedDict):
    """Permitted attributes for change
    [insert](https://docs.liquibase.com/change-types/insert.html).
    """

    insert: InsertAttributes


class ColumnAttributes(TypedDict):
    """Permitted attributes for `Colum.column`."""

    header: str
    index: int
    name: str
    type: str


class Column(TypedDict):
    """Permitted attributes for `[LoadDataAttributes | LoadUpdateDataAttributes].columns[*]`."""

    column: ColumnAttributes


class LoadDataAttributes(TypedDict):
    """Permitted attributes for `LoadData.loadData`."""

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


class LoadData(TypedDict):
    """Permitted attributes for change
    [loadData](https://docs.liquibase.com/change-types/load-data.html).
    """

    loadData: LoadDataAttributes
