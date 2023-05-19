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
)


class TestChangeSetAttributes(unittest.TestCase):
    def test_create_change_set_attributes(self):
        # Define test data
        test_data = {
            "author": "John Doe",
            "changes": [],
            "comment": "A comment",
            "contextFilter": "Some context filter",
            "created": "2022-01-01",
            "dbms": "MySQL",
            "id": "change_set_id",
            "failOnError": True,
            "ignore": False,
            "labels": "label1,label2",
            "logicalFilePath": "path/to/file.sql",
            "objectQuotingStrategy": "QUOTE_ALL_OBJECTS",
            "preConditions": [],
            "rollback": {},
            "runAlways": False,
            "runInTransaction": True,
            "runOnChange": False,
            "runOrder": "first",
            "runWith": None,
            "validCheckSum": "12345",
        }

        # Create instance of ChangeSetAttributes
        attributes = ChangeSetAttributes(**test_data)

        # Test instance attributes
        self.assertEqual(attributes["author"], test_data["author"])
        self.assertEqual(attributes["changes"], test_data["changes"])
        self.assertEqual(attributes["comment"], test_data["comment"])
        self.assertEqual(attributes["contextFilter"], test_data["contextFilter"])
        self.assertEqual(attributes["created"], test_data["created"])
        self.assertEqual(attributes["dbms"], test_data["dbms"])
        self.assertEqual(attributes["id"], test_data["id"])
        self.assertEqual(attributes["failOnError"], test_data["failOnError"])
        self.assertEqual(attributes["ignore"], test_data["ignore"])
        self.assertEqual(attributes["labels"], test_data["labels"])
        self.assertEqual(attributes["logicalFilePath"], test_data["logicalFilePath"])
        self.assertEqual(
            attributes["objectQuotingStrategy"], test_data["objectQuotingStrategy"]
        )
        self.assertEqual(attributes["preConditions"], test_data["preConditions"])
        self.assertEqual(attributes["rollback"], test_data["rollback"])
        self.assertEqual(attributes["runAlways"], test_data["runAlways"])
        self.assertEqual(attributes["runInTransaction"], test_data["runInTransaction"])
        self.assertEqual(attributes["runOnChange"], test_data["runOnChange"])
        self.assertEqual(attributes["runOrder"], test_data["runOrder"])
        self.assertEqual(attributes["runWith"], test_data["runWith"])
        self.assertEqual(attributes["validCheckSum"], test_data["validCheckSum"])


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


class TestDatabaseChangeLog(unittest.TestCase):
    def test_create_database_changelog(self):
        # Create instance of PreConditions
        database_change_log = DatabaseChangeLog(databaseChangeLog=[])
        # Test instance attributes
        self.assertIsInstance(database_change_log, dict)
        self.assertIsInstance(database_change_log["databaseChangeLog"], list)
        self.assertEqual(len(database_change_log["databaseChangeLog"]), 0)


if __name__ == "__main__":
    unittest.main()
