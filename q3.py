import pytest

import sqlite3


def get_table_information_from_database(database_filename):
    # Bring in code from question 1
    metadata_dictionary = {}
    return metadata_dictionary


def get_best_of_albums(database_filename, column_name_for_ordering):
    metadata_dictionary = get_table_information_from_database(database_filename)

    if column_name_for_ordering not in metadata_dictionary["albums"]:
        print("ERROR: could not find column '{}' in the list of columns for table 'albums'!".format(
            column_name_for_ordering))
        return []

    # create new sqlite connection here using the `database_filename` input
    # connection = ...

    result = []

    # with the context of `connection`
    #with connection:

        # obtain a cursor from the connection
        # cursor = ...

        # this should be a sql command  that returns all columns
        # from albums where the title contains "Greatest Hits" OR "Best Of"
        # the returned query data should be sorted according to the input `column_name_for_ordering`.
            # hint you can choose to use .format() on the string query to insert `column_name_for_ordering`.

        #stmt = ...

        # execute the command on the cursor
        # cursor.execute( ...

        # result = cursor.fetchall()

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