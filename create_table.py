from sqlalchemy import text
from database_engine import database_engine as ENGINE

def create_table():
    '''
    Fungsi untuk membuat tabel di dalam database
    args:
        None
    return:
        None
    '''
    # Membuat koneksi dengan database
    CONN = ENGINE().connect()

    # Membuat query untuk membuat tabel
    create_query = text(
        """
        CREATE TABLE items(
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_item TEXT NOT NULL,
            jumlah_item INTEGER NOT NULL CHECK(jumlah_item > 0),
            harga_item INTEGER NOT NULL CHECK(harga_item > 0),
            total_harga INTEGER NOT NULL,
            diskon INTEGER,
            harga_diskon INTEGER NOT NULL
        )
        """
    )

    # Apabila tidak ada kesalahan, membuat tabel di dalam database
    try:
        # Mengeksekusi query
        CONN.execute(create_query)

        # Melakukan commit untuk menyimpan perubahan di dalam database
        CONN.commit()
    # Apabila ada kesalahan, menampilkan pesan kesalahan
    except Exception as error:
        print(error)

        # Apabila ada kesalahan, mengembalikan database ke keadaan semula
        CONN.rollback()
    # Menutup koneksi dengan database setelah semua task dikerjakan
    finally:
        CONN.close()

create_table()