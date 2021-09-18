import pytest

import sqlite3


def get_best_of_albums_include_artists(database_filename):

    # create sqlite connection here using the `database_filename` input
    # connection = ...

    # obtain a cursor from the connection
    # cursor = ...

    # this should be a sql that returns all album ids, titles and artist names
    # from albums where the title contains "Greatest Hits" OR "Best Of"
    # the returned query data should be sorted according to the artists name.
    #
    # hint use an inner join to match albums to artists to get all necessary return types
    stmt = ""

    # execute the command on the cursor
    # cursor.execute( ...

    # Obtain result
    result = ()

    # Then close connection
    # connection. ...

    return result


def test_case1():
    database_filename = 'chinook.db'
    query_result = get_best_of_albums_include_artists(database_filename)

    print("(album id, album title, artist name):")
    for database_record in query_result:
        print(database_record)