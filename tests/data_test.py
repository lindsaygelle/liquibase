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
    ColumnAttributes,
    Delete,
    DeleteAttributes,
    Insert,
    InsertAttributes,
    LookupTable,
    Param,
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
        self.assertEqual(column_attributes["index"], test_data["header"])
        self.assertEqual(column_attributes["name"], test_data["header"])
        self.assertEqual(column_attributes["type"], test_data["header"])


if __name__ == "__main__":
    unittest.main()
