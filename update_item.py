def update_item_name(nama_item: str, update_nama_item: str, order_items: dict):
    '''
    Fungsi untuk mengupdate nama item yang telah dipesan sebelumnya
    args:
        nama_item (str): nama item yang ingin diubah
        update_nama_item (str): nama item yang baru
        order_items (dict): item yang telah dipesan beserta detailnya
    return:
        None
    '''
    # Memastikan nama_item ada di dalam order_items
    # Apabila ada, mengganti nama item tersebut
    try:
        order_items[update_nama_item] = order_items.pop(nama_item)

        print(f'{update_nama_item} berhasil ditambahkan!\n'
        f'Daftar barang yang Anda pesan adalah sebagai berikut: {order_items}')
    # Apabila tidak ada, menampilkan pesan kesalahan
    except KeyError as error:
        print(f'{update_nama_item} gagal ditambahkan. {error}. Silakan coba lagi.')

def update_item_qty(nama_item: str, update_jumlah_item: int, order_items: dict):
    '''
    Fungsi untuk mengupdate jumlah item yang telah dipesan sebelumnya
    args:
        nama_item (str): nama item yang jumlahnya ingin diubah
        update_jumlah_item (int): jumlah item yang baru
        order_items (dict): item yang telah dipesan beserta detailnya
    return:
        None
    '''
    # Memastikan nama_item ada di dalam order_items
    # Apabila ada, mengganti jumlah item tersebut
    try:
        order_items[nama_item][0] = update_jumlah_item
        
        print(f'Jumlah {nama_item.lower()} berhasil diubah!\n'
        f'Daftar barang yang Anda pesan adalah sebagai berikut: {order_items}')
    # Apabila tidak ada, menampilkan pesan kesalahan
    except KeyError as error:
        print(f'Pergantian jumlah {nama_item.lower()} gagal. {error}. Silakan coba lagi.')

def update_item_price(nama_item: str, update_harga_item: int, order_items: dict):
    '''
    Fungsi untuk mengupdate harga item yang telah dipesan sebelumnya
    args:
        nama_item (str): nama item yang harganya ingin diubah
        update_harga_item (int): harga item yang baru
        order_items (dict): item yang telah dipesan beserta detailnya
    return:
        None
    '''
    # Memastikan nama_item ada di dalam order_items
    # Apabila ada, mengganti harga item tersebut
    try:
        order_items[nama_item][1] = update_harga_item

        print(f'Harga {nama_item.lower()} berhasil diubah!\n'
        f'Daftar barang yang Anda pesan adalah sebagai berikut: {order_items}')
    # Apabila tidak ada, menampilkan pesan kesalahan
    except KeyError as error:
        print(f'Pergantian harga {nama_item.lower()} gagal. {error}. Silakan coba lagi.')