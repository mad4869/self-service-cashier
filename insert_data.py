from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

# Membuat engine yang terhubung dengan database
ENGINE = create_engine(
    'sqlite:///C:/Users/LENOVO/OneDrive/Desktop/Engineering/Pacmann/'
    'Python/Projects/database/project.db', 
    echo=True
    )

def create_table():
    '''
    Fungsi untuk membuat tabel di dalam database
    args:
        None
    return:
        transactions_table (obj): tabel transaksi yang akan diisi data item pesanan
    '''

    # Membuat objek metadata
    metadata = MetaData()

    # Membuat objek transactions_table dengan kolom-kolom sesuai data table_items
    transactions_table = Table('transactions', metadata,
    Column('transaction_id', Integer, primary_key=True),
    Column('nama_item', String),
    Column('jumlah_item', Integer),
    Column('harga_item', Integer),
    Column('total_harga', Integer),
    Column('diskon', Integer),
    Column('harga_diskon', Integer))

    # Memanggil fungsi untuk membuat tabel di dalam database
    metadata.create_all(ENGINE)

    return transactions_table

transactions_table = create_table()

def insert_to_table(table_items: dict):
    '''
    Fungsi untuk menyisipkan data ke dalam tabel
    args:
        table_items (dict): tabel data pesanan
    return:
        None
    '''
    
    # Membangun koneksi dengan database
    CONN = ENGINE.connect()

    # Apabila tidak ada kesalahan, memasukkan data ke dalam database
    try:
        # Iterasi untuk menyimpan data di dalam kolom table_items ke dalam variabel
        for (nama_item, jumlah_item, harga_item, total_harga, diskon, harga_diskon) in zip(
        table_items['Nama Item'], 
        table_items['Jumlah Item'], 
        table_items['Harga Item'], 
        table_items['Total Harga'], 
        table_items['Diskon'], 
        table_items['Harga Setelah Diskon']):
            
            # Memasukkan data variabel ke masing-masing kolom transactions_table
            insert = transactions_table.insert().values(
            nama_item=nama_item, 
            jumlah_item=jumlah_item,
            harga_item=harga_item,
            total_harga=total_harga,
            diskon=diskon,
            harga_diskon=harga_diskon
            )
            
            # Mengeksekusi perintah insert data
            CONN.execute(insert)
        
        # Melakukan commit untuk menyimpan perubahan pada tabel di database
        CONN.commit()
    
    # Jika ada kesalahan, mengembalikan database ke kondisi semula
    except:
        CONN.rollback()
    
    # Menutup koneksi dengan database
    finally:
        CONN.close()