# pylint: disable=C0114,C0115,C0116
import os
import sys
import unittest

current_file_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_file_dir, ".."))
sys.path.insert(0, parent_dir)

# pylint: disable=C0413
from liquibase.precondition import PreConditions


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


if __name__ == "__main__":
    unittest.main()
