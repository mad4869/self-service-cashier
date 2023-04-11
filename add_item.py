def add_item(nama_items: list, jumlah_items: list, harga_items: list):
    '''
    Fungsi untuk memasukkan masing-masing item ke dalam dictionary
    args:
        nama_items (list): nama item yang dipesan
        jumlah_items (list): jumlah item yang dipesan
        harga_items (list): harga item yang dipesan
    return:
        order_items (dict): item yang telah dipesan beserta detailnya
    '''
    
    order_items = {}
    
    # Memasangkan detail item dengan nama itemnya
    for i in range(len(nama_items)):
        order_items[nama_items[i].title()] = [jumlah_items[i], harga_items[i]]
    
    print(f'Daftar barang yang Anda pesan adalah sebagai berikut: {order_items}')

    return order_items