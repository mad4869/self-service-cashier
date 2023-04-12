from tabulate import tabulate
from insert_data import insert_to_table

def check_out(table_items: dict):
    '''
    Fungsi untuk menampilkan keseluruhan data pesanan dan memasukkannya ke dalam database
    args:
        table_items (dict): tabel data pesanan
    return:
        None
    '''
    diskon = []
    harga_diskon = []

    # Mengalkulasi diskon yang didapat pada tiap item
    for i in range(len(table_items['No'])):
        diskon_per_item = 0
        if table_items['Total Harga'][i] > 500_000:
            diskon_per_item = round(0.07 * table_items['Total Harga'][i])
        elif table_items['Total Harga'][i] > 300_000:
            diskon_per_item = round(0.06 * table_items['Total Harga'][i])
        elif table_items['Total Harga'][i] > 200_000:
            diskon_per_item = round(0.05 * table_items['Total Harga'][i])
        
        # Mengalkulasi harga tiap item setelah dikurangi diskon
        harga_diskon_per_item = table_items['Total Harga'][i] - diskon_per_item
        
        # Memasukkan diskon dan harga setelah diskon ke dalam list
        diskon.append(diskon_per_item)
        harga_diskon.append(harga_diskon_per_item)
    
    # Menambahkan list diskon dan harga setelah diskon ke dalam table_items
    table_items['Diskon'] = diskon
    table_items['Harga Setelah Diskon'] = harga_diskon
    
    # Menampilkan tabulasi keseluruhan data pesanan dan total harga yang harus dibayarkan
    print(f'Detail transaksi Anda adalah sebagai berikut:')
    print(tabulate(table_items, headers='keys', tablefmt='grid'))
    print(f'Total pembayaran Anda adalah sebesar: {sum(harga_diskon)}')

    # Mengeksekusi fungsi untuk memasukkan data ke dalam database
    insert_to_table(table_items)