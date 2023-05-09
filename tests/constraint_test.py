# pylint: disable=C0114,C0115,C0116
import os
import sys
import unittest

current_file_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_file_dir, ".."))
sys.path.insert(0, parent_dir)

# pylint: disable=C0413
from liquibase.constraint import AddCheckConstraint, CheckConstraint


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


if __name__ == "__main__":
    unittest.main()
