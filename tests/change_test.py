# pylint: disable=C0114,C0115,C0116
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# pylint: disable=C0413
from liquibase.change import (
    ChangeSetAttributes,
    DatabaseChangeLog,
    Property,
    PreConditions,
)


class TestChangeSet(unittest.TestCase):
    def test_change_set_attributes(self):
        # create an instance of ChangeSetAttributes
        change_set_attributes = ChangeSetAttributes(
            author="test_author",
            changes=[],
            comment="test comment",
            contextFilter="test filter",
            created="test created",
            dbms="test dbms",
            id="test id",
            failOnError=True,
            ignore=False,
            labels="test labels",
            logicalFilePath="test path",
            objectQuotingStrategy="LEGACY",
            preConditions=[],
            rollback={},
            runAlways=True,
            runInTransaction=True,
            runOnChange=True,
            runOrder="first",
            runWith=None,
            validCheckSum="test sum",
        )

        # check that each attribute is set correctly
        self.assertEqual(change_set_attributes["author"], "test_author")
        self.assertEqual(change_set_attributes["changes"], [])
        self.assertEqual(change_set_attributes["comment"], "test comment")
        self.assertEqual(change_set_attributes["contextFilter"], "test filter")
        self.assertEqual(change_set_attributes["created"], "test created")
        self.assertEqual(change_set_attributes["dbms"], "test dbms")
        self.assertEqual(change_set_attributes["id"], "test id")
        self.assertEqual(change_set_attributes["failOnError"], True)
        self.assertEqual(change_set_attributes["ignore"], False)
        self.assertEqual(change_set_attributes["labels"], "test labels")
        self.assertEqual(change_set_attributes["logicalFilePath"], "test path")
        self.assertEqual(change_set_attributes["objectQuotingStrategy"], "LEGACY")
        self.assertEqual(change_set_attributes["preConditions"], [])
        self.assertEqual(change_set_attributes["rollback"], {})
        self.assertEqual(change_set_attributes["runAlways"], True)
        self.assertEqual(change_set_attributes["runInTransaction"], True)
        self.assertEqual(change_set_attributes["runOnChange"], True)
        self.assertEqual(change_set_attributes["runOrder"], "first")
        self.assertEqual(change_set_attributes["runWith"], None)
        self.assertEqual(change_set_attributes["validCheckSum"], "test sum")


class TestPropertyAndPreConditions(unittest.TestCase):
    def test_property_and_preconditions(self):
        property_: Property = {
            "dbms": "mysql",
            "context": "dev",
            "file": "db.changelog.xml",
            "name": "key_name",
            "relativeToChangelogFile": True,
            "value": "value",
        }
        preconditions: PreConditions = {
            "preConditions": [
                {
                    "onFail": "HALT",
                    "not": {"dbms": "mysql", "runningAs": "root"},
                    "and": [
                        {"columnExists": {"tableName": "test", "columnName": "id"}}
                    ],
                }
            ]
        }
        self.assertEqual(property_["dbms"], "mysql")
        self.assertEqual(property_["context"], "dev")
        self.assertEqual(property_["file"], "db.changelog.xml")
        self.assertEqual(property_["name"], "key_name")
        self.assertTrue(property_["relativeToChangelogFile"])
        self.assertEqual(property_["value"], "value")
        self.assertIsInstance(preconditions, dict)
        self.assertIn("preConditions", preconditions)
        self.assertIsInstance(preconditions["preConditions"], list)
        self.assertIsInstance(preconditions["preConditions"][0], dict)
        self.assertIn("onFail", preconditions["preConditions"][0])
        self.assertEqual(preconditions["preConditions"][0]["onFail"], "HALT")
        self.assertIn("not", preconditions["preConditions"][0])
        self.assertIsInstance(preconditions["preConditions"][0]["not"], dict)
        self.assertIn("dbms", preconditions["preConditions"][0]["not"])
        self.assertEqual(preconditions["preConditions"][0]["not"]["dbms"], "mysql")
        self.assertIn("runningAs", preconditions["preConditions"][0]["not"])
        self.assertEqual(preconditions["preConditions"][0]["not"]["runningAs"], "root")
        self.assertIn("and", preconditions["preConditions"][0])
        self.assertIsInstance(preconditions["preConditions"][0]["and"], list)
        self.assertIsInstance(preconditions["preConditions"][0]["and"][0], dict)
        self.assertIn("columnExists", preconditions["preConditions"][0]["and"][0])
        self.assertIsInstance(
            preconditions["preConditions"][0]["and"][0]["columnExists"], dict
        )
        self.assertIn(
            "tableName", preconditions["preConditions"][0]["and"][0]["columnExists"]
        )
        self.assertEqual(
            preconditions["preConditions"][0]["and"][0]["columnExists"]["tableName"],
            "test",
        )
        self.assertIn(
            "columnName", preconditions["preConditions"][0]["and"][0]["columnExists"]
        )
        self.assertEqual(
            preconditions["preConditions"][0]["and"][0]["columnExists"]["columnName"],
            "id",
        )


class TestDatabaseChangeLog(unittest.TestCase):
    def test_database_change_log(self):
        db_changelog: DatabaseChangeLog = {"databaseChangeLog": []}
        self.assertIsInstance(db_changelog["databaseChangeLog"], list)


if __name__ == "__main__":
    unittest.main()
