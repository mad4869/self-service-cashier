from sqlalchemy import text
from database_engine import database_engine as ENGINE

def insert_to_table(table_items: dict):
    '''
    Fungsi untuk menyisipkan data ke dalam tabel
    args:
        table_items (dict): tabel data pesanan
    return:
        None
    '''
    # Membangun koneksi dengan database
    CONN = ENGINE().connect()

    # Membuat query untuk menyisipkan data ke dalam tabel
    insert_query = text(
        """
        INSERT INTO items(
            nama_item,
            jumlah_item,
            harga_item,
            total_harga,
            diskon,
            harga_diskon
        )
        VALUES(
            :nama_item,
            :jumlah_item,
            :harga_item,
            :total_harga,
            :diskon,
            :harga_diskon
        )
        """
    )

    # Apabila tidak ada kesalahan, memasukkan data ke dalam database
    try:
        # Mengakses data di list yang berada di masing-masing kolom tabel
        for (nama_item, jumlah_item, harga_item, total_harga, diskon, harga_diskon) in zip(
            table_items['Nama Item'],
            table_items['Jumlah Item'],
            table_items['Harga Item'],
            table_items['Total Harga'],
            table_items['Diskon'],
            table_items['Harga Setelah Diskon']):

            # Mengeksekusi query
            CONN.execute(insert_query, {
                'nama_item': nama_item,
                'jumlah_item': jumlah_item,
                'harga_item': harga_item,
                'total_harga': total_harga,
                'diskon': diskon,
                'harga_diskon': harga_diskon
                })
        
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