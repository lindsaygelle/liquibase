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
    AddForeignKeyConstraint,
    AddNotNullConstraint,
    AddPrimaryKey,
    AddUniqueConstraint,
    CheckConstraint,
    DefaultValue,
    ForeignKeyConstraint,
    NotNullConstraint,
    PrimaryKey,
    UniqueConstraint,
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

        # Test instance attributes
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

        # Test instance attributes
        self.assertEqual(add_default_value["defaultValue"], default_value)


class TestForeignKeyConstraint(unittest.TestCase):
    def test_foreign_key_constraint(self):
        # Define test data
        test_data: ForeignKeyConstraint = {
            "baseColumnNames": "id",
            "baseTableCatalogName": "orders",
            "baseTableName": "orders",
            "baseTableSchemaName": "public",
            "constraintName": "fk_orders_customer_id",
            "deferrable": True,
            "initiallyDeferred": True,
            "onDelete": "SET NULL",
            "onUpdate": "SET NULL",
            "referencedColumnNames": "id",
            "referencedTableCatalogName": "customers",
            "referencedTableName": "customers",
            "referencedTableSchemaName": "public",
            "validate": True,
        }

        # Create instance of ForeignKeyConstraint
        default_value = ForeignKeyConstraint(**test_data)

        # Test instance attributes
        self.assertEqual(default_value["baseColumnNames"], test_data["baseColumnNames"])
        self.assertEqual(
            default_value["baseTableCatalogName"], test_data["baseTableCatalogName"]
        )
        self.assertEqual(default_value["baseTableName"], test_data["baseTableName"])
        self.assertEqual(
            default_value["baseTableSchemaName"], test_data["baseTableSchemaName"]
        )
        self.assertEqual(default_value["constraintName"], test_data["constraintName"])
        self.assertEqual(default_value["deferrable"], test_data["deferrable"])
        self.assertEqual(
            default_value["initiallyDeferred"], test_data["initiallyDeferred"]
        )
        self.assertEqual(default_value["onDelete"], test_data["onDelete"])
        self.assertEqual(default_value["onUpdate"], test_data["onUpdate"])
        self.assertEqual(
            default_value["referencedColumnNames"], test_data["referencedColumnNames"]
        )
        self.assertEqual(
            default_value["referencedTableCatalogName"],
            test_data["referencedTableCatalogName"],
        )
        self.assertEqual(
            default_value["referencedTableName"], test_data["referencedTableName"]
        )
        self.assertEqual(
            default_value["referencedTableSchemaName"],
            test_data["referencedTableSchemaName"],
        )
        self.assertEqual(default_value["validate"], test_data["validate"])


class TestAddForeignKeyConstraint(unittest.TestCase):
    def test_add_foreign_key_constraint(self):
        test_data: ForeignKeyConstraint = {}
        # Create instance of ForeignKeyConstraint
        foreign_key_constraint = ForeignKeyConstraint(**test_data)
        # Create instance of AddForeignKeyConstraint
        add_foreign_key_constraint = AddForeignKeyConstraint(
            addForeignKeyConstraint=foreign_key_constraint
        )

        # Test instance attributes
        self.assertEqual(
            add_foreign_key_constraint["addForeignKeyConstraint"],
            foreign_key_constraint,
        )


class TestNotNullConstraint(unittest.TestCase):
    def test_not_null_constraint(self):
        # Define test data
        test_data: NotNullConstraint = {
            "catalogName": "my_catalog",
            "columnDataType": "varchar(55)",
            "columnName": "name",
            "constraintName": "customer_name",
            "defaultNullValue": "John",
            "schemaName": "public",
            "tableName": "customer",
            "validate": True,
        }

        # Create instance of NotNullConstraint
        not_null_constraint = NotNullConstraint(**test_data)

        # Test instance attributes
        self.assertEqual(not_null_constraint["catalogName"], test_data["catalogName"])
        self.assertEqual(
            not_null_constraint["columnDataType"], test_data["columnDataType"]
        )
        self.assertEqual(not_null_constraint["columnName"], test_data["columnName"])
        self.assertEqual(
            not_null_constraint["constraintName"], test_data["constraintName"]
        )
        self.assertEqual(
            not_null_constraint["defaultNullValue"], test_data["defaultNullValue"]
        )
        self.assertEqual(not_null_constraint["schemaName"], test_data["schemaName"])
        self.assertEqual(not_null_constraint["tableName"], test_data["tableName"])
        self.assertEqual(not_null_constraint["validate"], test_data["validate"])


class TestAddNotNullConstraint(unittest.TestCase):
    def test_add_not_null_constraint(self):
        test_data: NotNullConstraint = {}
        # Create instance of NotNullConstraint
        not_null_constraint = NotNullConstraint(**test_data)
        # Create instance of AddForeignKeyConstraint
        add_not_null_constraint = AddNotNullConstraint(
            addNotNullConstraint=not_null_constraint
        )

        # Test instance attributes
        self.assertEqual(
            add_not_null_constraint["addNotNullConstraint"],
            not_null_constraint,
        )


class TestPrimaryKey(unittest.TestCase):
    def test_primary_key(self):
        # Define test data
        test_data: PrimaryKey = {
            "catalogName": "my_catalog",
            "clustered": True,
            "columnNames": "id",
            "constraintName": "my_pk_constraint",
            "forIndexCatalogName": "my_index_catalog",
            "forIndexName": "my_index_name",
            "forIndexSchemaName": "my_index_schema",
            "schemaName": "my_schema",
            "tableName": "my_table",
            "tablespace": "my_tablespace",
            "validate": True,
        }

        # Create instance of PrimaryKey
        primary_key = PrimaryKey(**test_data)

        self.assertEqual(primary_key["catalogName"], test_data["catalogName"])
        self.assertEqual(primary_key["clustered"], test_data["clustered"])
        self.assertEqual(primary_key["columnNames"], test_data["columnNames"])
        self.assertEqual(primary_key["constraintName"], test_data["constraintName"])
        self.assertEqual(
            primary_key["forIndexCatalogName"], test_data["forIndexCatalogName"]
        )
        self.assertEqual(primary_key["forIndexName"], test_data["forIndexName"])
        self.assertEqual(
            primary_key["forIndexSchemaName"], test_data["forIndexSchemaName"]
        )
        self.assertEqual(primary_key["schemaName"], test_data["schemaName"])
        self.assertEqual(primary_key["tableName"], test_data["tableName"])
        self.assertEqual(primary_key["tablespace"], test_data["tablespace"])
        self.assertEqual(primary_key["validate"], test_data["validate"])


class TestAddPrimaryKey(unittest.TestCase):
    def test_add_primary_key(self):
        # Define test data
        test_data: PrimaryKey = {}
        # Create instance of NotNullConstraint
        primary_key = PrimaryKey(**test_data)
        # Create instance of AddForeignKeyConstraint
        add_primary_key = AddPrimaryKey(addPrimaryKey=primary_key)

        # Test instance attributes
        self.assertEqual(
            add_primary_key["addPrimaryKey"],
            primary_key,
        )


class TestUniqueConstraint(unittest.TestCase):
    def test_unique_constraint(self):
        # Define test data
        test_data: UniqueConstraint = {
            "catalogName": "my_catalog",
            "clustered": True,
            "columnNames": "name",
            "constraintName": "my_unique_constraint",
            "deferrable": True,
            "disabled": False,
            "forIndexCatalogName": "my_index_catalog",
            "forIndexName": "my_index_name",
            "forIndexSchemaName": "my_index_schema",
            "initiallyDeferred": False,
            "schemaName": "my_schema",
            "tableName": "my_table",
            "tablespace": "my_tablespace",
            "validate": True,
        }

        # Create instance of UniqueConstraint
        unique_constraint = UniqueConstraint(**test_data)

        # Test instance attributes
        self.assertEqual(unique_constraint["catalogName"], test_data["catalogName"])
        self.assertEqual(unique_constraint["clustered"], test_data["clustered"])
        self.assertEqual(unique_constraint["columnNames"], test_data["columnNames"])
        self.assertEqual(
            unique_constraint["constraintName"], test_data["constraintName"]
        )
        self.assertEqual(unique_constraint["deferrable"], test_data["deferrable"])
        self.assertEqual(unique_constraint["disabled"], test_data["disabled"])
        self.assertEqual(
            unique_constraint["forIndexCatalogName"], test_data["forIndexCatalogName"]
        )
        self.assertEqual(unique_constraint["forIndexName"], test_data["forIndexName"])
        self.assertEqual(
            unique_constraint["forIndexSchemaName"], test_data["forIndexSchemaName"]
        )
        self.assertEqual(
            unique_constraint["initiallyDeferred"], test_data["initiallyDeferred"]
        )
        self.assertEqual(unique_constraint["schemaName"], test_data["schemaName"])
        self.assertEqual(unique_constraint["tableName"], test_data["tableName"])
        self.assertEqual(unique_constraint["tablespace"], test_data["tablespace"])
        self.assertEqual(unique_constraint["validate"], test_data["validate"])


class TestAddUniqueConstraint(unittest.TestCase):
    def test_add_unique_constraint(self):
        # Define test data
        test_data: UniqueConstraint = {}
        # Create instance of UniqueConstraint
        unique_constraint = UniqueConstraint(**test_data)
        # Create instance of AddForeignKeyConstraint
        add_unique_constraint = AddUniqueConstraint(
            addUniqueConstraint=unique_constraint
        )

        # Test instance attributes
        self.assertEqual(
            add_unique_constraint["addUniqueConstraint"],
            unique_constraint,
        )


if __name__ == "__main__":
    unittest.main()
