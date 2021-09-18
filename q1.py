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



def test_case1():
    database_filename = 'chinook.db'
    metadata_dictionary = get_table_information_from_database(database_filename)

    tables = []
    for table in sorted(metadata_dictionary.keys()):
        tables.append(table)

    assert tables == ['albums', 'artists', 'customers', 'employees', 'genres', 'invoice_items', 'invoices', 'media_types', 'playlist_track', 'playlists', 'tracks']

    assert metadata_dictionary['albums'] == ['AlbumId', 'Title', 'ArtistId']
    assert metadata_dictionary['artists'] == ['ArtistId', 'Name']
    assert metadata_dictionary['customers'] == ['CustomerId', 'FirstName', 'LastName', 'Company', 'Address', 'City', 'State', 'Country', 'PostalCode', 'Phone', 'Fax', 'Email', 'SupportRepId']
    assert metadata_dictionary['employees'] == ['EmployeeId', 'LastName', 'FirstName', 'Title', 'ReportsTo', 'BirthDate', 'HireDate', 'Address', 'City', 'State', 'Country', 'PostalCode', 'Phone', 'Fax', 'Email']
    assert metadata_dictionary['genres'] == ['GenreId', 'Name']
    assert metadata_dictionary['invoice_items'] == ['InvoiceLineId', 'InvoiceId', 'TrackId', 'UnitPrice', 'Quantity']
    assert metadata_dictionary['invoices'] == ['InvoiceId', 'CustomerId', 'InvoiceDate', 'BillingAddress', 'BillingCity', 'BillingState', 'BillingCountry', 'BillingPostalCode', 'Total']
    assert metadata_dictionary['media_types'] == ['MediaTypeId', 'Name']
    assert metadata_dictionary['playlist_track'] == ['PlaylistId', 'TrackId']
    assert metadata_dictionary['playlists'] == ['PlaylistId', 'Name']
    assert metadata_dictionary['tracks'] == ['TrackId', 'Name', 'AlbumId', 'MediaTypeId', 'GenreId', 'Composer', 'Milliseconds', 'Bytes', 'UnitPrice']


