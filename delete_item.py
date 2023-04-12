def delete_item(nama_item: str, order_items: dict):
    '''
    Fungsi untuk menghapus data satu item
    args:
        nama_item (str): nama item yang ingin dihapus
        order_items (dict): item yang telah dipesan beserta detailnya
    return:
        None
    '''
    # Memastikan nama_item ada di dalam order_items
    # Apabila ada, menghapus data item tersebut 
    try:
        order_items.pop(nama_item)

        print(f'{nama_item} berhasil dihapus!\n'
              f'Daftar barang yang Anda pesan adalah sebagai berikut: {order_items}')
    # Apabila tidak ada, menampilkan pesan kesalahan
    except KeyError as error:
        print(f'Penghapusan gagal. {error}. Silakan coba lagi.')

def reset_transaction(order_items: dict):
    '''
    Fungsi untuk menghapus keseluruhan data pesanan
    args:
        order_items (dict): item yang telah dipesan beserta detailnya
    return:
        None
    '''
    order_items.clear()

    print('Semua barang pesanan anda telah dihapus!')