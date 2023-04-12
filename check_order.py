from tabulate import tabulate

def check_order(order_items: dict):
    '''
    Fungsi untuk menampilkan daftar pesanan dalam bentuk tabulasi
    args:
        order_items (dict): item yang telah dipesan beserta detailnya
    return:
        table_items (dict): daftar pesanan dalam bentuk tabel
    '''
    # Menampilkan pesan kesalahan apabila terdapat data yang missing di dalam order_items
    for key, value in order_items.items():
        if key == '' or len(value) != 2 or 0 in value or None in value:
            print('Terdapat kesalahan dalam input data. Silakan coba lagi.')
            return
    
    # Membuat tabel berdasarkan data di dalam order_items
    table_items = {}
    table_items['No'] = [i + 1 for i in range(len(order_items))]
    table_items['Nama Item'] = list(order_items.keys())
    table_items['Jumlah Item'] = [list(order_items.values())[i][0] for i in range(len(order_items))]
    table_items['Harga Item'] = [list(order_items.values())[i][1] for i in range(len(order_items))]
    table_items['Total Harga'] = (
        [(list(order_items.values())[i][0]) * (list(order_items.values())[i][1]) 
        for i in range(len(order_items))]
    )

    # Menampilkan pesan tidak ada kesalahan dan tabulasi data pesanan
    print('Tidak ada kesalahan dalam input data. Silakan cek kembali pesanan Anda:')
    print(tabulate(table_items, headers='keys', tablefmt='grid'))

    return table_items