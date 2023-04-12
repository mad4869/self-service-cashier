from sqlalchemy import text
from database_engine import engine as ENGINE

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
        for (nama_item, jumlah_item, harga_item, total_harga, diskon, harga_diskon) in zip(
            table_items['Nama Item'],
            table_items['Jumlah Item'],
            table_items['Harga Item'],
            table_items['Total Harga'],
            table_items['Diskon'],
            table_items['Harga Setelah Diskon']):

            CONN.execute(insert_query, {
                'nama_item': nama_item,
                'jumlah_item': jumlah_item,
                'harga_item': harga_item,
                'total_harga': total_harga,
                'diskon': diskon,
                'harga_diskon': harga_diskon
                })
        
        # Melakukan commit untuk menyimpan perubahan pada tabel di database
        CONN.commit()
    # Jika ada kesalahan, mengembalikan database ke kondisi semula
    except Exception as error:
        print(error)

        CONN.rollback()
    # Menutup koneksi dengan database
    finally:
        CONN.close()