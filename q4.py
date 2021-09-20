import pytest

import sqlite3

def get_best_of_albums_include_artists(database_filename):

    connection=sqlite3.connect(database_filename)

    cursor = connection.cursor()

    cursor.execute("SELECT albums.AlbumId, albums.Title, artist.Name \
                    FROM albums INNER JOIN artists artist \
                                ON albums.ArtistId = artist.ArtistId \
                                WHERE albums.Title LIKE '%Greatest Hits%' OR albums.Title LIKE '%Best Of%' ORDER BY artist.Name")

    result = cursor.fetchall()

    connection.close()

    return result


def test_case1():
    database_filename = 'chinook.db'
    query_result = get_best_of_albums_include_artists(database_filename)

    assert len(query_result)==21
    assert query_result[0] == (13, 'The Best Of Billy Cobham', 'Billy Cobham')
    assert query_result[10] == (36, 'Greatest Hits II', 'Queen')
    assert query_result[20] == (243, 'The Best Of Van Halen, Vol. I', 'Van Halen')