# pylint: disable=C0114,C0115,C0116
import os
import sys
import unittest

current_file_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_file_dir, ".."))
sys.path.insert(0, parent_dir)

# pylint: disable=C0413
from liquibase.constraint import (
    AddCheckConstraint,
    AddDefaultValue,
    CheckConstraint,
    DefaultValue,
)


class TestCheckConstraint(unittest.TestCase):
    def test_check_constraint(self):
        # Define test data
        test_data = {
            "catalogName": "my_catalog",
            "constraintBody": "my_constraint_body",
            "constraintName": "my_constraint_name",
            "disabled": True,
            "schemaName": "my_schema",
            "tableName": "my_table",
            "validate": False,
        }

        # Create instance of CheckConstraint
        check_constraint = CheckConstraint(**test_data)

        # Test instance attributes
        self.assertEqual(check_constraint["catalogName"], test_data["catalogName"])
        self.assertEqual(
            check_constraint["constraintBody"], test_data["constraintBody"]
        )
        self.assertEqual(
            check_constraint["constraintName"], test_data["constraintName"]
        )
        self.assertEqual(check_constraint["disabled"], test_data["disabled"])
        self.assertEqual(check_constraint["schemaName"], test_data["schemaName"])
        self.assertEqual(check_constraint["tableName"], test_data["tableName"])
        self.assertEqual(check_constraint["validate"], test_data["validate"])


class TestAddCheckConstraint(unittest.TestCase):
    def test_add_check_constraint(self):
        # Define test data
        test_data = {
            "catalogName": "my_catalog",
            "constraintBody": "my_constraint_body",
            "constraintName": "my_constraint_name",
            "disabled": True,
            "schemaName": "my_schema",
            "tableName": "my_table",
            "validate": False,
        }

        # Create instance of CheckConstraint
        check_constraint = CheckConstraint(**test_data)

        # Create instance of AddCheckConstraint
        add_check_constraint = AddCheckConstraint(addCheckConstraint=check_constraint)

        # Test instance attribute
        self.assertEqual(add_check_constraint["addCheckConstraint"], check_constraint)


class TestDefaultValue(unittest.TestCase):
    def test_default_value(self):
        # Define test data
        test_data: DefaultValue = {
            "catalogName": "my_catalog",
            "columnDataType": "varchar(255)",
            "columnName": "my_column",
            "defaultValue": "my_default_value",
            "defaultValueBoolean": False,
            "defaultValueComputed": "my_computed_value",
            "defaultValueConstraintName": "my_constraint",
            "defaultValueDate": "2022-05-10",
            "defaultValueNumeric": 123,
            "defaultValueSequenceNext": "my_sequence",
            "schemaName": "my_schema",
            "tableName": "my_table",
        }

        # Create instance of DefaultValue
        default_value = DefaultValue(**test_data)

        # Test instance attributes
        self.assertEqual(default_value["catalogName"], test_data["catalogName"])
        self.assertEqual(default_value["columnDataType"], test_data["columnDataType"])
        self.assertEqual(default_value["columnName"], test_data["columnName"])
        self.assertEqual(default_value["defaultValue"], test_data["defaultValue"])
        self.assertEqual(
            default_value["defaultValueBoolean"], test_data["defaultValueBoolean"]
        )
        self.assertEqual(
            default_value["defaultValueComputed"], test_data["defaultValueComputed"]
        )
        self.assertEqual(
            default_value["defaultValueConstraintName"],
            test_data["defaultValueConstraintName"],
        )
        self.assertEqual(
            default_value["defaultValueDate"], test_data["defaultValueDate"]
        )
        self.assertEqual(
            default_value["defaultValueNumeric"], test_data["defaultValueNumeric"]
        )
        self.assertEqual(
            default_value["defaultValueSequenceNext"],
            test_data["defaultValueSequenceNext"],
        )
        self.assertEqual(default_value["schemaName"], test_data["schemaName"])
        self.assertEqual(default_value["tableName"], test_data["tableName"])


class TestAddDefaultValue(unittest.TestCase):
    def test_add_default_value(self):
        test_data = {}
        # Create instance of DefaultValue
        default_value = DefaultValue(**test_data)
        # Create instance of AddDefaultValue
        add_default_value = AddDefaultValue(defaultValue=default_value)

        # Test instance attribute
        self.assertEqual(add_default_value["defaultValue"], default_value)


if __name__ == "__main__":
    unittest.main()
