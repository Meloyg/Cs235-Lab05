import sqlite3

from io import StringIO

# FIXXME: this is not needed when we use this code outside of coderunner!
def copy_file_db_to_memory_db(database_filename):
    # Read database to tempfile
    con = sqlite3.connect(database_filename)
    tempfile = StringIO()
    for line in con.iterdump():
        tempfile.write('%s\n' % line)
    con.close()
    tempfile.seek(0)

    mem_db = sqlite3.connect(":memory:")
    mem_db.cursor().executescript(tempfile.read())
    mem_db.commit()

    return mem_db


# destination database is only needed within coderunner
def save_favourite_songs(destination_database, employee_first_name, employee_last_name, artist):
    with destination_database:

        cursor = destination_database.cursor()

        try:
            stmt = "CREATE TABLE employee_favourite_tracks ( EmployeeId INTEGER NOT NULL, TrackId INTEGER NOT NULL, PRIMARY KEY(EmployeeId, TrackId), \
                    FOREIGN KEY(EmployeeId) REFERENCES employees(EmployeeId), FOREIGN KEY(TrackId) REFERENCES tracks(TrackId) )"

            cursor.execute(stmt)

            destination_database.commit()

        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            return

    select_stmt = "SELECT EmployeeId FROM employees WHERE FirstName = '{}' AND LastName = '{}'".format(
        employee_first_name, employee_last_name)

    cursor.execute(select_stmt)
    result = cursor.fetchone()
    if result is None:
        print("ERROR: Employee '{} {}' is not available in the database employees table!".format(employee_first_name,
                                                                                                 employee_last_name))
        return
    employeeid = result[0]

    select_stmt = "SELECT tracks.TrackId FROM tracks \
                   INNER JOIN albums album ON tracks.AlbumId = album.AlbumId \
                   INNER JOIN artists artist ON album.ArtistId = artist.ArtistId \
                   WHERE artist.Name = '{}'".format(artist)

    cursor.execute(select_stmt)
    trackids = cursor.fetchall()

    try:
        for track_id in trackids:
            track_id = track_id[0]
            stmt = "INSERT INTO employee_favourite_tracks VALUES({}, {})".format(employeeid, track_id)

            cursor.execute(stmt)

        destination_database.commit()

    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])



def test_case1():
    database_filename = 'chinook.db'
    database_in_memory = copy_file_db_to_memory_db(database_filename)

    employee_first_name = 'Margaret'
    employee_last_name = 'Park'
    artist = 'The Who'

    save_favourite_songs(database_in_memory, employee_first_name, employee_last_name, artist)

    stmt = "SELECT tracks.Name FROM tracks INNER JOIN employees employee INNER JOIN employee_favourite_tracks e_fav_t ON e_fav_t.EmployeeId=employee.EmployeeId WHERE employee.FirstName='{}' AND employee.LastName='{}' AND tracks.TrackId=e_fav_t.TrackId".format(
        employee_first_name, employee_last_name)

    tracks = database_in_memory.cursor().execute(stmt).fetchall()

    print("Favourite songs of '{} {}' from artist '{}'".format(employee_first_name, employee_last_name, artist))
    for song in tracks:
        song = song[0]
        print(song)


def test_case2():
    database_filename = 'chinook.db'
    database_in_memory = copy_file_db_to_memory_db(database_filename)

    employee_first_name = 'Jerry'
    employee_last_name = 'Lewis'
    artist = 'The Who'

    save_favourite_songs(database_in_memory, employee_first_name, employee_last_name, artist)

    stmt = "SELECT tracks.Name FROM tracks INNER JOIN employees employee INNER JOIN employee_favourite_tracks e_fav_t ON e_fav_t.EmployeeId=employee.EmployeeId WHERE employee.FirstName='{}' AND employee.LastName='{}' AND tracks.TrackId=e_fav_t.TrackId".format(
        employee_first_name, employee_last_name)

    tracks = database_in_memory.cursor().execute(stmt).fetchall()

def test_case3():
    database_filename = 'chinook.db'
    database_in_memory = copy_file_db_to_memory_db(database_filename)

    employee_first_name = 'Robert'
    employee_last_name = 'King'
    artist = 'Chicago Symphony Orchestra & Fritz Reiner'

    save_favourite_songs(database_in_memory, employee_first_name, employee_last_name, artist)

    stmt = "SELECT tracks.Name FROM tracks INNER JOIN employees employee INNER JOIN employee_favourite_tracks e_fav_t ON e_fav_t.EmployeeId=employee.EmployeeId WHERE employee.FirstName='{}' AND employee.LastName='{}' AND tracks.TrackId=e_fav_t.TrackId".format(
        employee_first_name, employee_last_name)

    tracks = database_in_memory.cursor().execute(stmt).fetchall()

    print("Favourite songs of '{} {}' from artist '{}'".format(employee_first_name, employee_last_name, artist))
    for song in tracks:
        song = song[0]
        print(song)

def test_case4():
    database_filename = 'chinook.db'
    database_in_memory = copy_file_db_to_memory_db(database_filename)

    employee_first_name = 'Laura'
    employee_last_name = 'Callahan'
    artist = 'Led Zeppelin'

    save_favourite_songs(database_in_memory, employee_first_name, employee_last_name, artist)

    stmt = "SELECT tracks.Name FROM tracks INNER JOIN employees employee INNER JOIN employee_favourite_tracks e_fav_t ON e_fav_t.EmployeeId=employee.EmployeeId WHERE employee.FirstName='{}' AND employee.LastName='{}' AND tracks.TrackId=e_fav_t.TrackId".format(
        employee_first_name, employee_last_name)

    tracks = database_in_memory.cursor().execute(stmt).fetchall()

    print("Favourite songs of '{} {}' from artist '{}'".format(employee_first_name, employee_last_name, artist))
    for song in tracks:
        song = song[0]
        print(song)
