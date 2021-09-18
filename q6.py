import sqlite3


def get_playlist(database_filename, which_playlist):
    connection = sqlite3.connect(database_filename)

    cursor = connection.cursor()

    cursor.execute("SELECT PlaylistId, Name FROM playlists WHERE Name='" + which_playlist + "'")

    result = cursor.fetchall()

    if len(result) == 0:
        print("ERROR: Could not find playlist '{}' in database!".format(which_playlist))
        return []

    playlist_id = result[0][0]
    # print(playlist_id)

    sql_stmt = "SELECT tracks.Name, album.Title, genre.Name, artist.Name, tracks.Composer FROM tracks \
                INNER JOIN albums album ON tracks.AlbumId=album.AlbumId \
                INNER JOIN genres genre ON tracks.GenreId=genre.GenreId \
                INNER JOIN artists artist ON album.ArtistId=artist.ArtistId \
                INNER JOIN playlist_track pt ON pt.PlaylistId = {} \
                WHERE tracks.TrackId = pt.TrackId ".format(playlist_id)

    cursor.execute(sql_stmt)

    result = cursor.fetchall()

    connection.close()

    return result


def test_case1():
    database_filename = 'chinook.db'
    which_playlist = 'On-The-Go 1'
    query_result = get_playlist(database_filename, which_playlist)

    print(f"Playlist '{which_playlist}'")
    for count, database_record in enumerate(query_result):
        print(f"{count:<2} Track Name: {database_record[0]}")
        print(f"   Album Title: {database_record[1]}")
        print(f"   Genre: {database_record[2]}")
        print(f"   Artist: {database_record[3]}")
        print(f"   Composer: {database_record[4]}")

def test_case2():
    database_filename = 'chinook.db'
    which_playlist = 'Heavy Metal Classic'
    query_result = get_playlist(database_filename, which_playlist)

    print(f"Playlist '{which_playlist}'")
    for count, database_record in enumerate(query_result):
        print(f"{count:<2} Track Name: {database_record[0]}")
        print(f"   Album Title: {database_record[1]}")
        print(f"   Genre: {database_record[2]}")
        print(f"   Artist: {database_record[3]}")
        print(f"   Composer: {database_record[4]}")

def test_case3():
    database_filename = 'chinook.db'
    which_playlist = 'Independent'
    query_result = get_playlist(database_filename, which_playlist)

    for database_record in query_result:
        print(database_record)

def test_case4():
    database_filename = 'chinook.db'
    which_playlist = 'Grunge'
    query_result = get_playlist(database_filename, which_playlist)

    for database_record in query_result:
        print(database_record)