from get_int import get_int

def input_item():
    '''
    Fungsi untuk menginput detail item yang ingin dipesan dan memasukkan data masing-masing item 
    ke dalam list
    args:
        None
    return:
        nama_items (list): list yang memuat nama item
        jumlah_items (list): list yang memuat jumlah item
        harga_items (list): list yang memuat harga item
    '''
    want_to_order = True
    nama_items = []
    jumlah_items = []
    harga_items = []

    # Memasukkan input ke dalam list selama user masih ingin memesan
    while want_to_order:
        # Mengambil input nama_item
        nama_item = input('Masukkan nama barang yang ingin dipesan: ').lower()
        
        # Memastikan nama_item tidak kosong
        while nama_item == '':
            print('Nama barang tidak boleh kosong. Silakan coba lagi.')
            nama_item = input('Masukkan nama barang yang ingin dipesan: ').lower()
        
        # Mengambil input jumlah_item
        jumlah_item = get_int(f'Masukkan jumlah {nama_item} yang ingin dipesan: ')

        # Memastikan jumlah_item lebih dari 0
        while jumlah_item <= 0:
            print(f'Jumlah {nama_item} harus lebih dari 0. Silakan coba lagi.')
            jumlah_item = get_int(f'Masukkan jumlah {nama_item} yang ingin dipesan: ')

        # Mengambil input harga_item
        harga_item = get_int(f'Masukkan harga {nama_item} yang ingin dipesan: ')

        # Memastikan harga_item lebih dari 0
        while jumlah_item <= 0:
            print(f'Harga {nama_item} harus lebih dari 0. Silakan coba lagi.')
            harga_item = get_int(f'Masukkan harga {nama_item} yang ingin dipesan: ')

        # Memasukkan tiap detail item ke masing-masing list
        nama_items.append(nama_item)
        jumlah_items.append(jumlah_item)
        harga_items.append(harga_item)

        # Memastikan apakah user masih ingin menambah item yang ingin dipesan
        while True:
            order_again = input('Apakah masih ada yang ingin dipesan (Ya/Tidak)? ').lower()
            if order_again == 'ya':
                break
            elif order_again == 'tidak':
                want_to_order = False
                break
            else:
                print('Perintah yang Anda masukkan salah. Silakan coba lagi')
    
    return nama_items, jumlah_items, harga_items

def input_update(prompt: str, order_items: dict):
    '''
    Fungsi untuk mengembalikan nama item yang datanya ingin diupdate
    args:
        prompt (str): prompt saat input data
        order_items (dict): item yang telah dipesan beserta detailnya
    return:
        nama_item (str): nama item yang datanya ingin diubah
    '''
    nama_item = (input(prompt)).title()

    # Memastikan nama_item ada di dalam order_items
    while nama_item not in order_items:
        print(f'Barang tidak ada dalam daftar pesanan Anda: {list(order_items.keys())}. Silakan coba lagi.')
        nama_item = (input(prompt)).title()
    
    return nama_item

def input_update_name(order_items: dict):
    '''
    Fungsi untuk mengembalikan nama item yang lama dan yang baru
    args:
        order_items (dict): item yang telah dipesan beserta detailnya
    return:
        nama_item (str): nama item yang lama
        nama_item_baru (str): nama item yang baru
    '''
    # Mengambil input nama item yang lama maupun yang baru
    nama_item = input_update('Masukkan nama barang yang ingin diupdate: ', order_items)
    nama_item_baru = (input('Masukkan nama barang yang baru: ')).title()

    # Memastikan nama_item_baru tidak kosong
    while nama_item_baru == '':
            print('Nama barang yang baru tidak boleh kosong. Silakan coba lagi.')
            nama_item_baru = input('Masukkan nama barang yang baru: ').title()

    # Memastikan nama_item_baru tidak sama dengan nama_item
    while nama_item_baru == nama_item:
        print(f'Nama barang yang baru tidak boleh sama dengan sebelumnya: {nama_item}')
        nama_item_baru = (input('Masukkan nama barang yang baru: ')).title()
    
    return nama_item, nama_item_baru

def input_update_qty(order_items: dict):
    '''
    Fungsi untuk mengembalikan nama item yang jumlahnya ingin diubah beserta jumlah yang baru
    args:
        order_items (dict): item yang telah dipesan beserta detailnya
    return:
        nama_item (str): nama item yang jumlahnya ingin diubah
        jumlah_item (int): jumlah item yang baru
    '''
    # Mengambil input nama dan jumlah item
    nama_item = input_update('Masukkan nama barang yang jumlahnya ingin diupdate: ', order_items)
    jumlah_item = get_int(f'Masukkan jumlah {nama_item.lower()} yang baru: ')

    # Memastikan jumlah_item lebih dari 0
    while jumlah_item <= 0:
            print(f'Jumlah {nama_item} harus lebih dari 0. Silakan coba lagi.')
            jumlah_item = get_int(f'Masukkan jumlah {nama_item} yang baru: ')

    # Memastikan jumlah_item tidak sama dengan jumlah_item di dalam order_items
    while jumlah_item == order_items[nama_item][0]:
        print(f'Jumlah {nama_item.lower()} tidak boleh sama dengan sebelumnya: {order_items[nama_item][0]}')
        jumlah_item = get_int(f'Masukkan jumlah {nama_item.lower()} yang baru: ')
    
    return nama_item, jumlah_item

def input_update_price(order_items: dict):
    '''
    Fungsi untuk mengembalikan nama item yang harganya ingin diubah beserta harga yang baru
    args:
        order_items (dict): item yang telah dipesan beserta detailnya
    return:
        nama_item (str): nama item yang harganya ingin diubah
        harga_item (int): harga item yang baru
    '''
    # Mengambil input nama dan harga item
    nama_item = input_update('Masukkan nama barang yang harganya ingin diupdate: ', order_items)
    harga_item = get_int(f'Masukkan harga {nama_item.lower()} yang baru: ')

    # Memastikan harga_item lebih dari 0
    while harga_item <= 0:
            print(f'Harga {nama_item} harus lebih dari 0. Silakan coba lagi.')
            harga_item = get_int(f'Masukkan harga {nama_item} yang baru: ')

    # Memastikan harga_item tidak sama dengan harga_item di dalam order_items
    while harga_item == order_items[nama_item][1]:
        print(f'Harga {nama_item.lower()} tidak boleh sama dengan sebelumnya: {order_items[nama_item][1]}')
        harga_item = get_int(f'Masukkan harga {nama_item.lower()} yang baru: ')
    
    return nama_item, harga_item

def input_delete(order_items: dict):
    '''
    Fungsi untuk mengembalikan nama item yang datanya ingin dihapus
    args:
        order_items (dict): item yang telah dipesan beserta detailnya
    return:
        nama item yang datanya ingin dihapus (str)
    '''
    
    return input_update('Masukkan nama barang yang ingin dihapus: ', order_items)