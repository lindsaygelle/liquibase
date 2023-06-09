# pylint: disable=C0114,C0115,C0116
from datetime import datetime
import os
import sys
import unittest

current_file_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_file_dir, ".."))
sys.path.insert(0, parent_dir)

# pylint: disable=C0413
from liquibase.data import (
    AddLookupTable,
    Column,
    ColumnAttributes,
    Delete,
    DeleteAttributes,
    Insert,
    InsertAttributes,
    LoadAttributes,
    LoadData,
    LoadDataAttributes,
    LoadUpdateDataAttributes,
    LoadUpdateData,
    LookupTable,
    MergeColumn,
    MergeColumns,
    Param,
    UpdateAttributes,
    Update,
    WhereParam,
)


class TestLookupTable(unittest.TestCase):
    def test_lookup_table(self):
        # Define test data
        test_data: LookupTable = {
            "constraintName": "my_constraint",
            "existingColumnName": "my_column",
            "existingTableCatalogName": "my_catalog",
            "existingTableName": "my_table",
            "existingTableSchemaName": "my_schema",
            "newColumnDataType": "VARCHAR(255)",
            "newColumnName": "my_column_1",
            "newTableCatalogName": "my_catalog_1",
            "newTableName": "my_table_1",
            "newTableSchemaName": "my_schema_1",
        }

        # Create instance of LookupTable
        lookup_table = LookupTable(**test_data)

        # Test instance attributes
        self.assertEqual(lookup_table["constraintName"], lookup_table["constraintName"])
        self.assertEqual(
            lookup_table["existingColumnName"], lookup_table["existingColumnName"]
        )
        self.assertEqual(
            lookup_table["existingTableCatalogName"],
            lookup_table["existingTableCatalogName"],
        )
        self.assertEqual(
            lookup_table["existingTableName"], lookup_table["existingTableName"]
        )
        self.assertEqual(
            lookup_table["existingTableSchemaName"],
            lookup_table["existingTableSchemaName"],
        )
        self.assertEqual(
            lookup_table["newColumnDataType"], lookup_table["newColumnDataType"]
        )
        self.assertEqual(lookup_table["newColumnName"], lookup_table["newColumnName"])
        self.assertEqual(
            lookup_table["newTableCatalogName"], lookup_table["newTableCatalogName"]
        )
        self.assertEqual(lookup_table["newTableName"], lookup_table["newTableName"])
        self.assertEqual(
            lookup_table["newTableSchemaName"], lookup_table["newTableSchemaName"]
        )


class TestAddLookupTable(unittest.TestCase):
    def test_add_lookup_table(self):
        # Define test data
        test_data: LookupTable = {}

        # Create instance of LookupTable
        lookup_table = LookupTable(**test_data)

        # Create instance of AddLookupTable
        add_lookup_table = AddLookupTable(addLookupTable=lookup_table)

        # Test instance attributes
        self.assertEqual(
            add_lookup_table["addLookupTable"],
            lookup_table,
        )


class TestParam(unittest.TestCase):
    def test_param(self):
        # Define test data
        test_data: Param = {
            "name": "A",
            "value": "VARCHAR(255)",
            "valueNumeric": 1,
            "valueBoolean": False,
            "valueDate": f"{datetime.now()}",
            "valueComputed": "CURRENT_TIME",
            "valueSequenceNext": "seq1",
            "valueSequenceCurrent": "seq2",
        }

        # Create instance of Param
        param = Param(**test_data)

        # Test instance attributes
        self.assertEqual(param["name"], test_data["name"])
        self.assertEqual(param["value"], test_data["value"])
        self.assertEqual(param["valueNumeric"], test_data["valueNumeric"])
        self.assertEqual(param["valueBoolean"], test_data["valueBoolean"])
        self.assertEqual(param["valueDate"], test_data["valueDate"])
        self.assertEqual(param["valueComputed"], test_data["valueComputed"])
        self.assertEqual(param["valueSequenceNext"], test_data["valueSequenceNext"])
        self.assertEqual(
            param["valueSequenceCurrent"], test_data["valueSequenceCurrent"]
        )


class TestWhereParam(unittest.TestCase):
    def test_where_param(self):
        # Define test data
        test_data: LookupTable = {}

        # Create instance of Param
        param = Param(**test_data)

        # Create instance of WhereParam
        where_param = WhereParam(param=param)

        # Test instance attributes
        self.assertEqual(
            where_param["param"],
            param,
        )


class TestDelete(unittest.TestCase):
    def test_delete_attributes(self):
        # Create instance of WhereParam
        where_param: WhereParam = {
            "name": "my_param",
            "value": "my_value",
            "valueNumeric": 1,
            "valueBoolean": True,
            "valueDate": "2023-05-11",
            "valueComputed": "my_expression",
            "valueSequenceNext": "my_sequence_next",
            "valueSequenceCurrent": "my_sequence_current",
        }

        # Define test data
        test_data = DeleteAttributes(
            catalogName="my_catalog",
            schemaName="my_schema",
            tableName="my_table",
            where="my_condition",
            whereParams=[{"param": where_param}],
        )

        # Create instance of Delete
        delete = Delete(delete=test_data)

        # Test instance attributes
        self.assertEqual(delete["delete"]["catalogName"], "my_catalog")
        self.assertEqual(delete["delete"]["schemaName"], "my_schema")
        self.assertEqual(delete["delete"]["tableName"], "my_table")
        self.assertEqual(delete["delete"]["where"], "my_condition")
        self.assertEqual(
            delete["delete"]["whereParams"][0]["param"]["name"], where_param["name"]
        )
        self.assertEqual(
            delete["delete"]["whereParams"][0]["param"]["value"], where_param["value"]
        )
        self.assertEqual(
            delete["delete"]["whereParams"][0]["param"]["valueNumeric"],
            where_param["valueNumeric"],
        )
        self.assertEqual(
            delete["delete"]["whereParams"][0]["param"]["valueBoolean"],
            where_param["valueBoolean"],
        )
        self.assertEqual(
            delete["delete"]["whereParams"][0]["param"]["valueDate"],
            where_param["valueDate"],
        )
        self.assertEqual(
            delete["delete"]["whereParams"][0]["param"]["valueComputed"],
            where_param["valueComputed"],
        )
        self.assertEqual(
            delete["delete"]["whereParams"][0]["param"]["valueSequenceNext"],
            where_param["valueSequenceNext"],
        )
        self.assertEqual(
            delete["delete"]["whereParams"][0]["param"]["valueSequenceCurrent"],
            where_param["valueSequenceCurrent"],
        )


class TestInsertAttributes(unittest.TestCase):
    def test_insert_attributes(self):
        # Define test data
        test_data: InsertAttributes = {
            "catalogName": "my_catalog",
            "columns": [{"name": "col1", "value": "val1"}],
            "dbms": "mysql",
            "schemaName": "my_schema",
            "tableName": "my_table",
        }
        # Create instance of InsertAttributes
        insert_attributes = InsertAttributes(**test_data)

        # Test instance attributes
        self.assertEqual(insert_attributes["catalogName"], test_data["catalogName"])
        self.assertEqual(insert_attributes["columns"], test_data["columns"])
        self.assertEqual(insert_attributes["dbms"], test_data["dbms"])
        self.assertEqual(insert_attributes["schemaName"], test_data["schemaName"])
        self.assertEqual(insert_attributes["tableName"], test_data["tableName"])


class TestInsert(unittest.TestCase):
    def test_insert(self):
        # Define test data
        test_data: InsertAttributes = {}
        # Create instance of InsertAttributes
        insert_attributes = InsertAttributes(**test_data)

        # Create instance of Insert
        insert = Insert(insert=insert_attributes)

        # Test instance attributes
        self.assertEqual(
            insert["insert"],
            insert_attributes,
        )


class TestColumnAttributes(unittest.TestCase):
    def test_column_attributes(self):
        # Define test data
        test_data: ColumnAttributes = {
            "header": "my_header",
            "index": 1,
            "name": "my_name",
            "type": "STRING",
        }
        # Create instance of ColumnAttributes
        column_attributes = ColumnAttributes(**test_data)

        # Test instance attributes
        self.assertEqual(column_attributes["header"], test_data["header"])
        self.assertEqual(column_attributes["index"], test_data["index"])
        self.assertEqual(column_attributes["name"], test_data["name"])
        self.assertEqual(column_attributes["type"], test_data["type"])


class TestColumn(unittest.TestCase):
    def test_column(self):
        # Define test data
        test_data: ColumnAttributes = {}

        # Create instance of ColumnAttributes
        column_attributes = ColumnAttributes(**test_data)

        # Create instance of Column
        column = Column(column=column_attributes)

        # Test instance attributes
        self.assertEqual(
            column["column"],
            column_attributes,
        )


class TestLoadAttributes(unittest.TestCase):
    def test_load_attributes(self):
        # Define test data
        test_data: LoadAttributes = {
            "catalogName": "my_catalog",
            "columns": [],
            "commentLineStartsWith": "test",
            "encoding": "utf-8",
            "file": "my_file.sql",
            "quotchar": "'",
            "relativeToChangelogFile": True,
            "schemaName": "my_schema",
            "separator": "",
            "tableName": "my_table",
            "usePreparedStatements": False,
        }

        # Create instance of LoadAttributes
        load_attributes = LoadAttributes(**test_data)

        # Test instance attributes
        self.assertEqual(load_attributes["catalogName"], test_data["catalogName"])
        self.assertEqual(load_attributes["columns"], test_data["columns"])
        self.assertEqual(
            load_attributes["commentLineStartsWith"], test_data["commentLineStartsWith"]
        )
        self.assertEqual(load_attributes["encoding"], test_data["encoding"])
        self.assertEqual(load_attributes["file"], test_data["file"])
        self.assertEqual(load_attributes["quotchar"], test_data["quotchar"])
        self.assertEqual(
            load_attributes["relativeToChangelogFile"],
            test_data["relativeToChangelogFile"],
        )
        self.assertEqual(load_attributes["schemaName"], test_data["schemaName"])
        self.assertEqual(load_attributes["separator"], test_data["separator"])
        self.assertEqual(load_attributes["tableName"], test_data["tableName"])
        self.assertEqual(
            load_attributes["usePreparedStatements"], test_data["usePreparedStatements"]
        )


class TestLoadDataAttributes(unittest.TestCase):
    def test_load_data_attributes(self):
        # Define test data
        test_data: LoadDataAttributes = {
            "catalogName": "my_catalog",
            "columns": [],
            "commentLineStartsWith": "test",
            "encoding": "utf-8",
            "file": "my_file.sql",
            "onlyUpdate": True,
            "primaryKey": False,
            "quotchar": "'",
            "relativeToChangelogFile": True,
            "schemaName": "my_schema",
            "separator": "",
            "tableName": "my_table",
            "usePreparedStatements": False,
        }

        # Create instance of LoadDataAttributes
        load_data_attributes = LoadDataAttributes(**test_data)

        # Test instance attributes
        self.assertEqual(load_data_attributes["catalogName"], test_data["catalogName"])
        self.assertEqual(load_data_attributes["columns"], test_data["columns"])
        self.assertEqual(
            load_data_attributes["commentLineStartsWith"],
            test_data["commentLineStartsWith"],
        )
        self.assertEqual(load_data_attributes["encoding"], test_data["encoding"])
        self.assertEqual(load_data_attributes["file"], test_data["file"])
        self.assertEqual(load_data_attributes["onlyUpdate"], test_data["onlyUpdate"])
        self.assertEqual(load_data_attributes["primaryKey"], test_data["primaryKey"])
        self.assertEqual(load_data_attributes["quotchar"], test_data["quotchar"])
        self.assertEqual(
            load_data_attributes["relativeToChangelogFile"],
            test_data["relativeToChangelogFile"],
        )
        self.assertEqual(load_data_attributes["schemaName"], test_data["schemaName"])
        self.assertEqual(load_data_attributes["separator"], test_data["separator"])
        self.assertEqual(load_data_attributes["tableName"], test_data["tableName"])
        self.assertEqual(
            load_data_attributes["usePreparedStatements"],
            test_data["usePreparedStatements"],
        )


class TestLoadData(unittest.TestCase):
    def test_load_data(self):
        # Define test data
        test_data: LoadDataAttributes = {}

        # Create instance of LoadDataAttributes
        load_data_attributes = LoadDataAttributes(**test_data)

        # Create instance of LoadData
        load_data = LoadData(loadData=load_data_attributes)

        # Test instance attributes
        self.assertEqual(
            load_data["loadData"],
            load_data_attributes,
        )


class TestLoadUpdateData(unittest.TestCase):
    def test_load_update_data(self):
        # Define test data
        test_data: LoadUpdateDataAttributes = {}

        # Create instance of LoadDataAttributes
        load_update_data_attributes = LoadUpdateDataAttributes(**test_data)

        # Create instance of LoadUpdateData
        load_update_data = LoadUpdateData(loadUpdateData=load_update_data_attributes)

        # Test instance attributes
        self.assertEqual(
            load_update_data["loadUpdateData"],
            load_update_data_attributes,
        )


class TestMergeColumn(unittest.TestCase):
    def test_merge_column(self):
        # Define test data
        test_data: MergeColumn = {
            "catalogName": "my_catalog",
            "column1Name": "column1",
            "column2Name": "column2",
            "finalColumnName": "merged_column",
            "finalColumnType": "varchar(255)",
            "joinString": ",",
            "schemaName": "my_schema",
            "tableName": "my_table",
        }

        # Create instance of MergeColumn
        merge_column = MergeColumn(**test_data)

        # Test instance attributes
        self.assertEqual(merge_column["catalogName"], test_data["catalogName"])
        self.assertEqual(merge_column["column1Name"], test_data["column1Name"])
        self.assertEqual(merge_column["column2Name"], test_data["column2Name"])
        self.assertEqual(merge_column["finalColumnName"], test_data["finalColumnName"])
        self.assertEqual(merge_column["finalColumnType"], test_data["finalColumnType"])
        self.assertEqual(merge_column["joinString"], test_data["joinString"])
        self.assertEqual(merge_column["schemaName"], test_data["schemaName"])
        self.assertEqual(merge_column["tableName"], test_data["tableName"])


class TestMergeColumns(unittest.TestCase):
    def test_merge_columns(self):
        # Define test data
        test_data: MergeColumn = {
            "catalogName": "my_catalog",
            "column1Name": "column1",
            "column2Name": "column2",
            "finalColumnName": "merged_column",
            "finalColumnType": "varchar(255)",
            "joinString": ",",
            "schemaName": "my_schema",
            "tableName": "my_table",
        }

        # Create instance of MergeColumn
        merge_column = MergeColumn(**test_data)

        # Create instance of MergeColumns
        merge_columns = MergeColumns(mergeColumns=merge_column)

        # Test instance attributes
        self.assertEqual(
            merge_columns["mergeColumns"],
            merge_column,
        )


class TestUpdateAttributes(unittest.TestCase):
    def test_update_attributes(self):
        # Define test data
        test_data: UpdateAttributes = {
            "catalogName": "my_catalog",
            "columnName": "my_column",
            "newDataType": "varchar(255)",
            "schemaName": "my_schema",
            "tableName": "my_table",
            "where": "id = 1",
            "whereParam": [],
        }

        # Create instance of UpdateAttributes
        update_attributes = UpdateAttributes(**test_data)

        # Test instance attributes
        self.assertEqual(update_attributes["catalogName"], test_data["catalogName"])
        self.assertEqual(update_attributes["columnName"], test_data["columnName"])
        self.assertEqual(update_attributes["newDataType"], test_data["newDataType"])
        self.assertEqual(update_attributes["schemaName"], test_data["schemaName"])
        self.assertEqual(update_attributes["tableName"], test_data["tableName"])
        self.assertEqual(update_attributes["where"], test_data["where"])
        self.assertEqual(update_attributes["whereParam"], test_data["whereParam"])


class TestUpdate(unittest.TestCase):
    def test_update(self):
        # Define test data
        test_data: UpdateAttributes = {
            "catalogName": "my_catalog",
            "columnName": "my_column",
            "newDataType": "varchar(255)",
            "schemaName": "my_schema",
            "tableName": "my_table",
            "where": "id = 1",
            "whereParam": [],
        }

        # Create instance of UpdateAttributes
        update_attributes = UpdateAttributes(**test_data)

        # Create instance of Update
        update = Update(update=update_attributes)

        # Test instance attributes
        self.assertEqual(
            update["update"],
            update_attributes,
        )


if __name__ == "__main__":
    unittest.main()
