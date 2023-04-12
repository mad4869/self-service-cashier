from sqlalchemy import text
from database_engine import database_engine as ENGINE

def select_table():
    '''
    Fungsi untuk melihat data tabel yang berada di dalam database
    args:
        None
    return:
        None
    '''
    # Membuat koneksi dengan database
    CONN = ENGINE().connect()

    # Membuat query untuk melihat data di dalam tabel
    select_query = text(
        """
        SELECT * FROM items
        """
    )

    # Mengeksekusi query
    table = CONN.execute(select_query)

    # Menampilkan tiap baris yang berada di dalam tabel
    for row in table:
            print(row)

    # Menutup koneksi dengan database setelah semua task dikerjakan
    CONN.close()