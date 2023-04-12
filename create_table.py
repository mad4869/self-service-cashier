from sqlalchemy import text
from database_engine import engine as ENGINE

def create_table():
    '''
    Fungsi untuk membuat tabel di dalam database
    args:
        None
    return:
        None
    '''
    CONN = ENGINE().connect()

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
    try:
        CONN.execute(create_query)
        CONN.commit()
    except Exception as error:
        print(error)
        
        CONN.rollback()
    finally:
        CONN.close()

create_table()
# CONN = ENGINE().connect()
# CONN.execute(text("DELETE FROM items WHERE nama_item = 'Majalah'"))
# CONN.commit()
# CONN.close()