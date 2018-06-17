import csv
import sqlite3

import pandas as pd
from query_library import *


def convert_csv_to_database():
    # Create database.
    conn = sqlite3.connect('database_name.db')
    cursor = conn.cursor()
    # Create table.
    cursor.execute("""DROP TABLE IF EXISTS table_name""")
    cursor.execute("""CREATE TABLE table_name (primary_key INTEGER, fruit_type TEXT, units_of_fruit INTEGER,
    sale_price REAL)""")
    conn.commit()
    # Load CSV file into CSV reader.
    with open('CSV_file_name.csv', 'r') as csv_file:
        # Iterate through CSV file and remove NULL byts. NOTE: NULL byts cause code error.
        csv_reader = csv.reader(null_byts.replace('\0', '') for null_byts in csv_file)
        # Iterate through CSV file and insert values into database.
        for database_values in csv_reader:
            cursor.execute("""INSERT INTO table_name
            VALUES (?,?,?,?)""", database_values)
    # Close the CSV file and commit changes to database.
    csv_file.close()
    conn.commit()


def query_database(sql):
    # Connect to database
    conn = sqlite3.connect('database_name.db')
    cursor = conn.cursor()
    # Query database
    cursor.execute(sql)
    # Return data
    return cursor.fetchall()


def query_database_print(sql):
    # Connect to database
    conn = sqlite3.connect('database_name.db')
    cursor = conn.cursor()
    # Query database
    cursor.execute(sql)
    # Print data
    print(cursor.fetchall())


def query_database_export_to_excel(sql, file_name, excel_sheet_name, start_row, start_col):
    # Connect to database
    conn = sqlite3.connect('database_name.db')
    # Return dataframe from a SQL query
    dataframe = pd.read_sql_query(sql, conn)
    # Create an Excel file using XlsxWriter as the engine
    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
    # Convert the dataframe to an XlsxWriter Excel object and write to sheets
    dataframe.to_excel(writer, sheet_name=excel_sheet_name, index=False, na_rep='NULL', startrow=start_row, startcol=start_col)
    # Close the Excel writer and output the Excel file.
    writer.save()


def query_database_export_to_csv(sql, file_name):  # Define file name as string i.e "file_name.csv"
    # Connect to database
    conn = sqlite3.connect('database_name.db')
    cursor = conn.cursor()
    # Return data from database via SQL.
    cursor.execute(sql)
    query_data = cursor.fetchall()
    # Export data to CSV file.
    with open(file_name, 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(query_data)


def close_database():
    # Connect to database.
    conn = sqlite3.connect('database_name.db')
    cursor = conn.cursor()
    # Drop tables.
    cursor.execute("""DROP TABLE table_name""")
    # Close database connection.
    conn.close()


def main():
    print("Testing...")
    convert_csv_to_database()
    query_database_print(test_query)
    query_database_export_to_excel(test_query, "test.xlsx", "Test_Sheet", 0, 0)
    query_database_export_to_csv(test_query, "test.csv")
    close_database()


# Run program.
if __name__ == "__main__":
    main()

