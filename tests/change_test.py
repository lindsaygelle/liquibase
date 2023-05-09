# pylint: disable=C0114,C0115,C0116
import os
import sys
import unittest

current_file_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_file_dir, ".."))
sys.path.insert(0, parent_dir)

# pylint: disable=C0413
from liquibase.change import (
    ChangeSet,
    ChangeSetAttributes,
    DatabaseChangeLog,
    PreConditions,
)


class TestChangeSetAttributes(unittest.TestCase):
    def test_create_change_set_attributes(self):
        # Define test data
        test_data = {
            "author": "John Doe",
            "changes": [],
            "comment": "A comment",
            "context_filter": "Some context filter",
            "created": "2022-01-01",
            "dbms": "MySQL",
            "id_": "change_set_id",
            "fail_on_error": True,
            "ignore": False,
            "labels": "label1,label2",
            "logical_file_path": "path/to/file.sql",
            "object_quoting_strategy": "QUOTE_ALL_OBJECTS",
            "pre_conditions": [],
            "rollback": {},
            "run_always": False,
            "run_in_transaction": True,
            "run_on_change": False,
            "run_order": "first",
            "run_with": None,
            "valid_checksum": "12345",
        }

        # Create instance of ChangeSetAttributes
        attributes = ChangeSetAttributes(**test_data)

        # Test instance attributes
        self.assertEqual(attributes["author"], test_data["author"])
        self.assertEqual(attributes["changes"], test_data["changes"])
        self.assertEqual(attributes["comment"], test_data["comment"])
        self.assertEqual(attributes["contextFilter"], test_data["context_filter"])
        self.assertEqual(attributes["created"], test_data["created"])
        self.assertEqual(attributes["dbms"], test_data["dbms"])
        self.assertEqual(attributes["id"], test_data["id_"])
        self.assertEqual(attributes["failOnError"], test_data["fail_on_error"])
        self.assertEqual(attributes["ignore"], test_data["ignore"])
        self.assertEqual(attributes["labels"], test_data["labels"])
        self.assertEqual(attributes["logicalFilePath"], test_data["logical_file_path"])
        self.assertEqual(
            attributes["objectQuotingStrategy"], test_data["object_quoting_strategy"]
        )
        self.assertEqual(attributes["preConditions"], test_data["pre_conditions"])
        self.assertEqual(attributes["rollback"], test_data["rollback"])
        self.assertEqual(attributes["runAlways"], test_data["run_always"])
        self.assertEqual(
            attributes["runInTransaction"], test_data["run_in_transaction"]
        )
        self.assertEqual(attributes["runOnChange"], test_data["run_on_change"])
        self.assertEqual(attributes["runOrder"], test_data["run_order"])
        self.assertEqual(attributes["runWith"], test_data["run_with"])
        self.assertEqual(attributes["validCheckSum"], test_data["valid_checksum"])


class TestChangeSet(unittest.TestCase):
    def test_create_change_set(self):
        # Define test data
        test_data = {"author": "John Doe", "changes": [], "id": "change_set_id"}
        # Create instance of ChangeSetAttributes
        attributes = ChangeSetAttributes(**test_data)
        # Create instance of ChangeSet
        change_set = ChangeSet(changeSet=attributes)
        # Test instance attributes
        self.assertIsInstance(change_set, dict)
        self.assertEqual(change_set["changeSet"], attributes)


class TestPreConditions(unittest.TestCase):
    def test_create_preconditions(self):
        # Create instance of PreConditions
        pre_conditions = PreConditions(
            preConditions=[{"onFail": "CONTINUE", "dbms": {"type": "h2"}}]
        )
        # Test instance attributes
        self.assertIsInstance(pre_conditions, dict)
        self.assertIsInstance(pre_conditions["preConditions"], list)
        self.assertEqual(len(pre_conditions["preConditions"]), 1)
        self.assertIsInstance(pre_conditions["preConditions"][0], dict)
        self.assertEqual(pre_conditions["preConditions"][0]["onFail"], "CONTINUE")
        self.assertIsInstance(pre_conditions["preConditions"][0]["dbms"], dict)
        self.assertEqual(pre_conditions["preConditions"][0]["dbms"]["type"], "h2")


class TestDatabaseChangeLog(unittest.TestCase):
    def test_create_database_changelog(self):
        # Create instance of PreConditions
        database_change_log = DatabaseChangeLog(databaseChangeLog=[])
        # Test instance attributes
        self.assertIsInstance(database_change_log, dict)
        self.assertIsInstance(database_change_log["databaseChangeLog"], list)
        self.assertEqual(len(database_change_log["databaseChangeLog"]), 1)


if __name__ == "__main__":
    unittest.main()
