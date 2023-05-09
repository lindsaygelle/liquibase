# Liquibase
This repository contains the Python API for Liquibase. The package provides a way to programmatically generate database changes for Liquibase using Python. It aims to allow users to manage database changes using Python code, providing typing, autocomplete and extensibility for developers. It provides several submodules that can be imported based on your development needs. The package is intended to match the Liquibase changelog specification as closely as possible, but is not maintained by their core team.

##  Installation
To use the Liquibase package, you must first install Liquibase on your system. You can download Liquibase from the [official website](https://www.liquibase.com/). After installing Liquibase, you can install the Python API by running the following command:

## Usage
To use the Liquibase package in your Python code, you must first import the liquibase module:

```python
from liquibase import <module>
```

You can then use the liquibase module to create various Liquibase change objects, such as creating a [table](/liquibase/entity.py):

```python
from liquibase.entity import Column, CreateTable, Table, TableColumn

CreateTable(
    createTable=Table(
        catalogName="animals",
        columns=[TableColumn(column=Column(name="id", value="INT"))],
        remarks="Animals table",
        schemaName="public",
        tableName="animals",
        tablespace=None,
    )
)
```

Or an entire database changelog:

```python
from liquibase.change import ChangeSet, ChangeSetAttributes, DatabaseChangeLog
from liquibase.entity import CreateView, View

DatabaseChangeLog(
    databaseChangeLog=[
        ChangeSet(
            changeSet=ChangeSetAttributes(
                author="lindsaygelle",
                changes=[
                    CreateView(
                        view=View(
                            selectQuery="SELECT * FROM animal", viewName="animals"
                        )
                    )
                ],
                id="1.0.0",
            )
        )
    ]
)
```

Of course, you can combine the models with any standard Python function to generate a bulk of tables, views, or functions based on your own requirements!

```python
# Import the required changes.
from liquibase.change import (
    ChangeSet,
    ChangeSetAttributes,
    DatabaseChangeLog,
)
# Import the required change properties. Here I am creating some tables.
from liquibase.entity import Column, ColumnConstraint, CreateTable, Table, TableColumn

# Anything else to make the change!
import semver

AUTHOR = "example"
version = semver.version.Version(major=0, minor=0, patch=0)

# Create the container to store all the change logs.
change_logs = []

# Create the database change log. Liquibase requires this.
database_change_log = DatabaseChangeLog(databaseChangeLog=change_logs)

for i in [1, 2, 3]:
    table_name = f"table_{i}"
    version = version.bump_major()

    # Create the container for the changes for the change set.
    change_set_attributes_changes = [

        CreateTable(
            createTable=Table(
                columns=[
                    TableColumn(
                        column=Column(
                            autoIncrement=True,
                            constraints=ColumnConstraint(
                                primaryKey=True,
                                primaryKeyName="pk_id",
                                referencedColumnNames="id",
                                referencedTableName=table_name,
                            ),
                            name="id",
                            type="INT",
                        )
                    )
                ],
                tableName=table_name,
            )
        )
    ]

    # Create the attributes for the change set.
    change_set_attributes = ChangeSetAttributes(
        author=AUTHOR, changes=change_set_attributes_changes, id=f"{version}"
    )
    # Create the change set. Change sets are required for entity changes.
    change_set = ChangeSet(changeSet=change_set_attributes)

    # Add change to the database change log.
    change_logs.append(change_set)
```

Don't forget the dump the results:

```python
import json

print(json.dumps(database_change_log, indent=4, sort_keys=True))
```

Output for Liquibase to use:

```json
{
    "databaseChangeLog": [
        {
            "changeSet": {
                "author": "example",
                "changes": [
                    {
                        "createTable": {
                            "columns": [
                                {
                                    "column": {
                                        "autoIncrement": true,
                                        "constraints": {
                                            "primaryKey": true,
                                            "primaryKeyName": "pk_id",
                                            "referencedColumnNames": "id",
                                            "referencedTableName": "table_3"
                                        },
                                        "name": "id",
                                        "type": "INT"
                                    }
                                }
                            ],
                            "tableName": "table_3"
                        }
                    }
                ],
                "id": "3.0.0"
            }
        }
    ]
}
```

## Notices
Liquibase is based on the [documentation](https://docs.liquibase.com/) by the Liquibase developers. It is not maintained by their core team and is an experimental project. I authored the code so that I could simplify writing changelogs in Python. Because of that, the classes provided may not always match what is found in the Liquibase core code. If that doesn't bother you and you wish to extend the code found here, awesome! Happy developing.

## Getting Started
Assuming that you have a supported version of Python installed, you can first set up your environment by creating a virtual environment:

```sh
# Create the virtual environment.
$ python -m venv .venv
```

```sh
# Activate the virtual environment.
$ . .venv/bin/activate
```

Then, you can install the Liquibase package from source with:

```sh
$ git clone https://github.com/lindsaygelle/liquibase.git
$ cd liquibase
$ python -m pip install -r requirements.txt
$ python -m pip install -e .
```

# Getting Help
We use GitHub issues for tracking bugs and feature requests, but have limited bandwidth to address them. If you think you have found a bug, please open an issue.

## Contributing
We value feedback and contributions from our community. Whether it's a bug report, new feature, correction, or additional documentation, we welcome your issues and pull requests. Please read through our [CONTRIBUTING](./CONTRIBUTING.md) document before submitting any issues or pull requests to ensure we have all the necessary information to effectively respond to your contribution.

## License
The Liquibase package is released under the MIT License. Please see the [LICENSE](./LICENSE) file for more information.
