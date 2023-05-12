# pylint: disable=C0114,C0115,C0116
import os
import sys
import unittest

current_file_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_file_dir, ".."))
sys.path.insert(0, parent_dir)

# pylint: disable=C0413
from liquibase.data import AddLookupTable, LookupTable


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


class AddTestLookupTable(unittest.TestCase):
    def test_add_lookup_table(self):
        # Define test data
        test_data: LookupTable = {}

        # Create instance of LookupTable
        lookup_table = LookupTable(**test_data)

        # Create instance of AddForeignKeyConstraint
        add_lookup_table = AddLookupTable(addLookupTable=lookup_table)

        # Test instance attributes
        self.assertEqual(
            add_lookup_table["addLookupTable"],
            lookup_table,
        )


if __name__ == "__main__":
    unittest.main()
