import pytest

import sqlite3


def get_all_artists_with_at_least_n_albums(database_filename, n):

    # create sqlite connection here using the `database_filename` input
    # connection = ...

    # obtain a cursor from the connection
    # cursor = ...

    # this should be a sql that returns all artist ids, artist names, and the Number of albums
    # The returned tuples should only include artists with greater than or equal to `n` parameter
    # album count.
    # The returned dataset should be ordered by the number of albums descending, and if the number is the same, then
    # by the artists name ascending.
    #
    # The returned dataset should not have multiple tuples for the same artist
    # - the count of albums should be together in 1 tuple representing the artist.
    # - Hint: use `GROUP BY`
    #
    # Hint: use an inner join to match artists to albums to get all necessary return types
    stmt = ""

    # execute the command on the cursor
    # cursor.execute( ...

    # Obtain result
    result = ()

    # Then close connection
    # code here

    return result


def test_case1():
    database_filename = 'chinook.db'
    n = 4
    query_result = get_all_artists_with_at_least_n_albums(database_filename, n)

    print("(artist id, artist name, number of albums):")
    for database_record in query_result:
        print(database_record)


def test_case2():
    database_filename = 'chinook.db'
    n = 8
    query_result = get_all_artists_with_at_least_n_albums(database_filename, n)

    print("(artist id, artist name, number of albums):")
    for database_record in query_result:
        print(database_record)

        
def test_case3():
    database_filename = 'chinook.db'
    n = 2
    query_result = get_all_artists_with_at_least_n_albums(database_filename, n)

    for database_record in query_result:
        print(database_record)