import pytest

import sqlite3


def get_table_information_from_database(database_filename):
    connection = sqlite3.connect(database_filename)

    metadata_dictionary = {}

    with connection:
        cursor = connection.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

        result = cursor.fetchall()

        table_names = []

        for row in result:
            if not "sqlite" in row[0]:
                table_names.append(row[0])

        for table_name in table_names:

            stmt = "PRAGMA table_info('{}')".format(table_name)
            cursor.execute(stmt)

            columns = cursor.fetchall()

            for column in columns:
                if table_name in metadata_dictionary:
                    metadata_dictionary[table_name].append(column[1])
                else:
                    metadata_dictionary[table_name] = [column[1]]

    return metadata_dictionary


def get_best_of_albums(database_filename, column_name_for_ordering):
    metadata_dictionary = get_table_information_from_database(database_filename)
    if column_name_for_ordering not in metadata_dictionary["albums"]:
        print("ERROR: could not find column '{}' in the list of columns for table 'albums'!".format(
            column_name_for_ordering))
        return []

    connection = sqlite3.connect(database_filename)

    result = []

    with connection:
        cursor = connection.cursor()

        stmt = "SELECT * FROM albums WHERE Title LIKE '%Greatest Hits%' OR Title Like '%Best Of%' ORDER BY {}".format(
            column_name_for_ordering)
        cursor.execute(stmt)

        result = cursor.fetchall()

    return result


def test_case1():
    database_filename = 'chinook.db'
    column_name_for_ordering = "ArtistId"
    query_result = get_best_of_albums(database_filename, column_name_for_ordering)

    print("(album id, album title, artist id):")
    for database_record in query_result:
        print(database_record)

def test_case2():
    database_filename = 'chinook.db'
    column_name_for_ordering = "AlbumId"
    query_result = get_best_of_albums(database_filename, column_name_for_ordering)

    print("(album id, album title, artist id):")
    for database_record in query_result:
        print(database_record)

def test_case3():
    database_filename = 'chinook.db'
    column_name_for_ordering = "Id"
    query_result = get_best_of_albums(database_filename, column_name_for_ordering)

    for database_record in query_result:
        print(database_record)

def test_case4():
    database_filename = 'chinook.db'
    column_name_for_ordering = "Title"
    query_result = get_best_of_albums(database_filename, column_name_for_ordering)

    for database_record in query_result:
        print(database_record)