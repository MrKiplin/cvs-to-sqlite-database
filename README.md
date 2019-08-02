# cvs-to-sqlite-database

Convert CSV file to sqlite database. Includes functions for exporting data to various formats.

## Extra functions

- Query database
- Export data to excel files
- Export data to CSV file

## Getting Started

Code will require some customizing to account for new CSV files.

### Prerequisites

Requires panda module if exporting to excel is required. install using pip.

```
pip pandas
```

### Table Settings

Step 1: Setting table columns. Give your table columns a name and assign the data types.

```
CREATE TABLE table_name (--insert column names and types here--)
```

**Data Types:**

- NULL. The value is a NULL value.
- INTEGER. The value is a signed integer, stored in 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.
- REAL. The value is a floating point value, stored as an 8-byte IEEE floating point number.
- TEXT. The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE).
- BLOB. The value is a blob of data, stored exactly as it was input.

Step 2: Add the same number of question marks as columns there are in the table.

```
VALUES (?,?,?,?)
```

### Hack Excel formatting

[Formatting excel columns](https://xlsxwriter.readthedocs.io/example_pandas_column_formats.html) - Docs

## Authors

![](mrkiplin-icon.gif)

- **Theo Jones** - _Initial work_ - [MrKiplin](https://github.com/MrKiplin)
