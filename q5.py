import pytest

import sqlite3

def get_all_artists_with_at_least_n_albums(database_filename, n):

    connection=sqlite3.connect(database_filename)

    cursor = connection.cursor()

    cursor.execute("SELECT artists.artistId, artists.Name, COUNT(album.AlbumId) AS NrAlbums \
                    FROM artists INNER JOIN albums album \
                                ON album.ArtistId = artists.ArtistId \
                                GROUP BY artists.Name \
                                HAVING NrAlbums >= " + str(n) + \
                                " ORDER BY NrAlbums DESC, artists.Name ASC")

    result = cursor.fetchall()

    connection.close()

    return result


def test_case1():
    database_filename = 'chinook.db'
    n = 4
    query_result = get_all_artists_with_at_least_n_albums(database_filename, n)
    assert len(query_result) == 12
    print("(artist id, artist name, number of albums):")
    assert query_result[11] == (21, 'Various Artists', 4)


def test_case2():
    database_filename = 'chinook.db'
    n = 8
    query_result = get_all_artists_with_at_least_n_albums(database_filename, n)
    assert len(query_result) == 5
    assert query_result[4] == (150, 'U2', 10)


def test_case3():
    database_filename = 'chinook.db'
    n = 2
    query_result = get_all_artists_with_at_least_n_albums(database_filename, n)
    assert len(query_result) == 56
    assert query_result[55] == (146, 'Titas', 2)