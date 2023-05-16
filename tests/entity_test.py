# pylint: disable=C0114,C0115,C0116
import os
import sys
import unittest

current_file_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_file_dir, ".."))
sys.path.insert(0, parent_dir)

# pylint: disable=C0413
from liquibase.entity import AddAutoIncrement, AutoIncrement


class TestAutoIncrement(unittest.TestCase):
    def test_auto_increment(self):
        test_data: AutoIncrement = {
            "catalogName": "my_catalog",
            "columnDataType": "VARCHAR(255)",
            "columnName": "my_column",
            "defaultOnNull": True,
            "generationType": "any",
            "incrementBy": 1,
            "schemaName": "my_schema",
            "startWith": "test",
            "tableName": "my_table",
        }
        auto_increment = AutoIncrement(**test_data)
        self.assertEqual(auto_increment["catalogName"], test_data["catalogName"])
        self.assertEqual(auto_increment["columnDataType"], test_data["columnDataType"])
        self.assertEqual(auto_increment["columnName"], test_data["columnName"])
        self.assertEqual(auto_increment["defaultOnNull"], test_data["defaultOnNull"])
        self.assertEqual(auto_increment["generationType"], test_data["generationType"])
        self.assertEqual(auto_increment["incrementBy"], test_data["incrementBy"])
        self.assertEqual(auto_increment["schemaName"], test_data["schemaName"])
        self.assertEqual(auto_increment["startWith"], test_data["startWith"])
        self.assertEqual(auto_increment["tableName"], test_data["tableName"])


class TestAddAutoIncrement(unittest.TestCase):
    def test_auto_increment(self):
        test_data: AutoIncrement = {
            "catalogName": "my_catalog",
            "columnDataType": "VARCHAR(255)",
            "columnName": "my_column",
            "defaultOnNull": True,
            "generationType": "any",
            "incrementBy": 1,
            "schemaName": "my_schema",
            "startWith": "test",
            "tableName": "my_table",
        }
        auto_increment = AutoIncrement(**test_data)
        add_auto_increment = AddAutoIncrement(addAutoIncrement=auto_increment)
        self.assertEqual(
            add_auto_increment["addAutoIncrement"],
            auto_increment,
        )


if __name__ == "__main__":
    unittest.main()
