# Liquibase
This repository contains the Python API for Liquibase. The API provides a way to programmatically generate database changes for Liquibase using Python. It aims to allow users to manage database changes using Python code, providing typing, autocomplete and extensibility for developers. It provides several submodules that can be imported based on your development needs. The package is intended to match the Liquibase changelog specification as closely as possible, but is not maintained by their core team.

##  Installation
To use the Liquibase Python API, you must have Liquibase installed on your system. You can download Liquibase from the official website https://www.liquibase.org/. After installing Liquibase, you can install the Python API by running the following command:

## Usage
To use the Liquibase package in your Python code, you must first import the liquibase module:

```python
from liquibase import <module>
```

You can then use the liquibase module to create various Liquibase change objects, such as creating a table:

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

## Notices
Liquibase is based on the [documentation](https://docs.liquibase.com/) by the Liquibase developers. It is not maintained by their core team and is an experimental project. I authored the code so that I could simplify writing changelogs in Python. Because of that, the classes provided may not always match what is found in the Liquibase core code. If that doesn't bother you and you wish to extend the code found here, awesome! Happy developing.

## Getting Started
Assuming that you have a supported version of Python installed, you can first set up your environment with:

```sh
$ python -m venv .venv
...
$ . .venv/bin/activate
```

Then, you can install liquibase from source with:

```sj
$ git clone https://github.com/lindsaygelle/liquibase.git
$ cd liquibase
$ python -m pip install -r requirements.txt
$ python -m pip install -e .
```

## Contributing
We value feedback and contributions from our community. Whether it's a bug report, new feature, correction, or additional documentation, we welcome your issues and pull requests. Please read through this CONTRIBUTING document before submitting any issues or pull requests to ensure we have all the necessary information to effectively respond to your contribution.

## License
The Liquibase Python API is released under the MIT License. Please see the [LICENSE](./LICENSE) file for more information.
