# Super Cashier
Super Cashier adalah program berbasis python yang dirancang agar seorang pelanggan dapat memasukkan sendiri item serta jumlah dan harga item ke dalam daftar pesanan yang kemudian akan disimpan di dalam SQLite database.
<br><br>

# Background
Seorang pemilik supermarket besar di salah satu kota di Indonesia memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu membuat sistem kasir self-service dengan harapan:
- Pelanggan bisa langsung memasukkan item, jumlah item, dan harga item yang dibeli serta beberapa fitur lain.
- Pelanggan yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut.
<br>

# Requirements
Beberapa fitur program yang dibutuhkan pada Super Cashier antara lain:
1. Pelanggan dapat memasukkan nama, jumlah, dan harga item ke dalam daftar pesanan
2. Pelanggan dapat memperbarui nama, jumlah, dan harga item yang telah dimasukkan sebelumnya
3. Pelanggan dapat menghapus salah satu atau seluruh item dari daftar pesanan
4. Pelanggan dapat memeriksa ulang daftar pesanan yang telah dibuat
5. Pelanggan dapat menerima diskon jika memenuhi syarat pembelian
6. Pelanggan dapat melihat total pembayaran dari keseluruhan transaksi
7. Program dapat menyimpan data pesanan ke dalam database
<br>

# Alur Program
![A flowchart image that explains how the program runs](https://i.imgur.com/APH7xhq.jpg)
**START**

1. Pelanggan akan diminta memasukkan nama item, jumlah item, dan harga item secara berurutan melalui fungsi `input_item()`<br>
`input_item()` akan memastikan apakah pelanggan masih ingin menambah pesanan. Jika ya, pelanggan akan diminta untuk memasukkan nama, jumlah, dan harga item berikutnya. Jika pelanggan sudah selesai memasukkan item, `input_item()` akan berhenti bekerja dan mengembalikan nilai nama, jumlah, dan harga item dalam bentuk list.
2. List nama, jumlah, dan harga item diproses oleh fungsi `add_item()` yang akan memasangkan item dan detail item ke dalam dictionary `order_items`
3. Jika pelanggan ingin mengubah data di dalam pesanan, pelanggan bisa menggunakan fitur **update.** Terdapat tiga fitur update:
    - update nama item: `input_update_name()` akan meminta pelanggan memasukkan nama item sebelumnya dan nama item yang akan menggantikan. `update_item_name()` akan mengganti nama item di dalam `order_items` sesuai input dari pelanggan.
    - update jumlah item: `input_update_qty()` akan meminta pelanggan memasukkan nama item yang jumlahnya ingin diganti dan jumlah item yang baru. `update_item_qty()` akan mengganti jumlah item di dalam `order_items` sesuai input dari pelanggan.
    - update harga item: `input_update_price()` akan meminta pelanggan memasukkan nama item yang harganya ingin diganti dan harga item yang baru. `update_item_price()` akan mengganti harga item di dalam `order_items` sesuai input dari pelanggan.
4. Jika pelanggan ingin menghapus data di dalam pesanan, pelanggan bisa menggunakan fitur **delete.** Terdapat dua fitur delete:
    - hapus per item: `input_delete()` akan meminta pelanggan memasukkan nama item yang ingin dihapus. `delete_item()` akan menghapus item di dalam `order_items` sesuai input dari pelanggan.
    - hapus seluruh item: method `reset_transaction()` akan menghapus seluruh isi `order_items`<br> Pelanggan dapat menambahkan item kembali melalui `input_item()`
5. Pelanggan dapat melakukan pengecekan terhadap item yang telah dipesan melalui fungsi `check_order()` yang akan memastikan tidak adanya kesalahan input.<br>
Jika ada, pesan kesalahan ditampilkan dan pelanggan diarahkan kembali menuju `input_item()` <br>
Jika tidak ada, data pesanan akan ditampilkan dalam `table_items` yang berisi kolom:
    - No.
    - Nama item
    - Jumlah item
    - Harga per item
    - Total harga
6. Jika pelanggan tidak menemukan kesalahan dalam daftar pesanan, pelanggan dapat melakukan check out melalui fungsi `check_out()`<br> 
`check_out()` akan menampilkan data pesanan dan pelanggan akan menerima diskon:
    - 5% jika total harga lebih dari 200.000,
    - 6% jika total harga lebih dari 300.000,
    - 7% jika total harga lebih dari 500.000.<br>
    Data pesanan akan menampilkan `table_items` yang telah ditambahkan kolom:
    - Diskon
    - Harga setelah diskon<br>
    serta akan menampilkan total pembayaran dari seluruh item.<br> 
    Terakhir, `check_out` akan memanggil fungsi `insert_to_table()` untuk memasukkan data ke dalam database.

**END** 
<br><br>
# Penjelasan Code
**input_item()**<br>

`input_item()` meminta pelanggan untuk memasukkan nama, jumlah, dan harga item selama pelanggan masih ingin menambah pesanan. Method ini menggunakan bantuan modul `input_int` pada input nilai integer untuk menghandle `ValueError`.
```
def input_int(prompt: str):
    '''
    Fungsi untuk menghandle Value Error saat menginput nilai integer
    args:
        prompt (str): prompt saat input data
    return:
        nilai yang dimasukkan user (int)
    '''
    while True:
        # Mengembalikan nilai integer jika data yang dimasukkan benar
        try: 
            return int(input(prompt))
        # Memberikan feedback apabila data yang dimasukkan bukan integer
        except ValueError as error:
            print(f'{error}. Mohon untuk memasukkan angka. Silakan coba lagi')
```
```
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
```
Selama nilai `want_to_order = True`, input dijalankan dan nilainya dimasukkan ke dalam list `nama_items`, `jumlah_items`, dan `harga_items`.
```
    want_to_order = True
    nama_items = []
    jumlah_items = []
    harga_items = []
```
`nama_item` diambil dengan built-in `input()`, dan sebelum dimasukkan ke dalam list dipastikan tidak kosong.<br>
`jumlah_item` dan `harga_item` diambil dengan method `input_int()` lalu dipastikan lebih dari 0.
Kemudian memastikan pelanggan ingin menambah pesanan atau tidak: jika ya, looping kembali ke awal; jika tidak, `want_to_order = False` dan looping berhenti.
```
    while want_to_order:
        # Mengambil input nama_item
        nama_item = input('Masukkan nama barang yang ingin dipesan: ').lower()
        
        # Memastikan nama_item tidak kosong
        while nama_item == '':
            print('Nama barang tidak boleh kosong. Silakan coba lagi.')
            nama_item = input('Masukkan nama barang yang ingin dipesan: ').lower()
        
        # Mengambil input jumlah_item
        jumlah_item = input_int(f'Masukkan jumlah {nama_item} yang ingin dipesan: ')

        # Memastikan jumlah_item lebih dari 0
        while jumlah_item <= 0:
            print(f'Jumlah {nama_item} harus lebih dari 0. Silakan coba lagi.')
            jumlah_item = input_int(f'Masukkan jumlah {nama_item} yang ingin dipesan: ')

        # Mengambil input harga_item
        harga_item = input_int(f'Masukkan harga {nama_item} yang ingin dipesan: ')

        # Memastikan harga_item lebih dari 0
        while jumlah_item <= 0:
            print(f'Harga {nama_item} harus lebih dari 0. Silakan coba lagi.')
            harga_item = input_int(f'Masukkan harga {nama_item} yang ingin dipesan: ')

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
``` 
Setelah semua item diinput, mengembalikan list `nama_items`, `jumlah_items`, dan `harga_items`.
```
    return nama_items, jumlah_items, harga_items
```
---
**add_item()**<br>
`add_item()` menerima argumen berupa list `nama_items`, `jumlah_items`, dan `harga_items` lalu mengembalikannya dalam bentuk dictionary `order_items` yang keynya adalah `nama_item` dan valuenya berupa list berisi `jumlah_item` dan `harga_item`.
```
def add_item(nama_items: list, jumlah_items: list, harga_items: list):
    '''
    Fungsi untuk memasukkan masing-masing item ke dalam daftar pesanan
    args:
        nama_items (list): nama item yang dipesan
        jumlah_items (list): jumlah item yang dipesan
        harga_items (list): harga item yang dipesan
    return:
        order_items (dict): item yang telah dipesan beserta detailnya
    '''
```
Melakukan looping sesuai banyaknya item yang sudah dimasukkan pelanggan, memasangkan key `nama_item` dengan list `[jumlah_item, harga_item]` di dalam `order_items`, dan mengembalikan `order_items`.
```
    order_items = {}
    
    # Memasangkan detail item dengan nama itemnya
    for i in range(len(nama_items)):
        order_items[nama_items[i].title()] = [jumlah_items[i], harga_items[i]]
    
    print(f'Daftar barang yang Anda pesan adalah sebagai berikut: {order_items}')

    return order_items
```
---
**input_update_name()**<br>
`input_update_name()` meminta pelanggan memasukkan nama item yang ingin diganti dan nama item baru secara berurutan.<br>
Method ini menggunakan bantuan modul `input_update` untuk memverifikasi apakah nama item yang ingin diganti ada di dalam `order_items`.
```
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
```
```
def input_update_name(order_items: dict):
    '''
    Fungsi untuk mengembalikan nama item yang lama dan yang baru
    args:
        order_items (dict): item yang telah dipesan beserta detailnya
    return:
        nama_item (str): nama item yang lama
        nama_item_baru (str): nama item yang baru
    '''
```
`nama_item` didapatkan dengan method `input_update()`.<br> 
`nama_item_baru` didapatkan dengan built-in `input()`, dipastikan tidak kosong dan tidak sama dengan `nama_item`.<br>
Terakhir, mengembalikan `nama_item` dan `nama_item_baru`. 
```
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
```
---
**update_item_name()**<br>
`update_item_name()` menerima `nama_item`, `nama_item_baru`, dan `order_items` sebagai argumen, lalu mengganti key `nama_item` di dalam `order_items` dengan key `nama_item_baru`.
```
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
```
Kode dijalankan dalam blok `try` dan `except` untuk menghandle `KeyError` apabila key `nama_item` tidak ditemukan di dalam `order_items`.<br>
Jika tidak ada error, menghapus key `nama_item` lalu mengassign valuenya ke key `nama_item_baru`.<br>
Jika ada error, menampilkan pesan kesalahan.
```
    # Memastikan nama_item ada di dalam order_items
    # Apabila ada, mengganti nama item tersebut
    try:
        order_items[update_nama_item] = order_items.pop(nama_item)

        print(f'{update_nama_item} berhasil ditambahkan!\n'
        f'Daftar barang yang Anda pesan adalah sebagai berikut: {order_items}')
    # Apabila tidak ada, menampilkan pesan kesalahan
    except KeyError as error:
        print(f'{update_nama_item} gagal ditambahkan. {error}. Silakan coba lagi.')
```
---
**input_update_qty()**<br>
`input_update_qty()` meminta pelanggan memasukkan nama item yang jumlahnya ingin diganti dan jumlah item yang baru secara berurutan.<br>
```
def input_update_qty(order_items: dict):
    '''
    Fungsi untuk mengembalikan nama item yang jumlahnya ingin diubah beserta jumlah yang baru
    args:
        order_items (dict): item yang telah dipesan beserta detailnya
    return:
        nama_item (str): nama item yang jumlahnya ingin diubah
        update_jumlah_item (int): jumlah item yang baru
    '''
```
`nama_item` didapatkan dengan method `input_update()`.<br> 
`update_jumlah_item` didapatkan dengan method `input_int()`, dipastikan lebih dari 0 dan tidak sama dengan jumlah item sebelumnya.<br>
Terakhir, mengembalikan `nama_item` dan `update_jumlah_item`. 
```
    # Mengambil input nama dan jumlah item
    nama_item = input_update('Masukkan nama barang yang jumlahnya ingin diupdate: ', order_items)
    update_jumlah_item = input_int(f'Masukkan jumlah {nama_item.lower()} yang baru: ')

    # Memastikan jumlah_item lebih dari 0
    while update_jumlah_item <= 0:
            print(f'Jumlah {nama_item} harus lebih dari 0. Silakan coba lagi.')
            update_jumlah_item = input_int(f'Masukkan jumlah {nama_item} yang baru: ')

    # Memastikan jumlah_item tidak sama dengan jumlah_item di dalam order_items
    while update_jumlah_item == order_items[nama_item][0]:
        print(f'Jumlah {nama_item.lower()} tidak boleh sama dengan sebelumnya: {order_items[nama_item][0]}')
        update_jumlah_item = input_int(f'Masukkan jumlah {nama_item.lower()} yang baru: ')
    
    return nama_item, update_jumlah_item
```
---
**update_item_qty()**<br>
`update_item_qty()` menerima `nama_item`, `update_jumlah_item`, dan `order_items` sebagai argumen, lalu mengganti jumlah `nama_item` di dalam `order_items` dengan `update_jumlah_item`.
```
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
```
Kode dijalankan dalam blok `try` dan `except` untuk menghandle `KeyError` apabila key `nama_item` tidak ditemukan di dalam `order_items`.<br>
Jika tidak ada error, mengassign value jumlah item pada key `nama_item` kepada `update_jumlah_item`.<br>
Jika ada error, menampilkan pesan kesalahan.
```
    # Memastikan nama_item ada di dalam order_items
    # Apabila ada, mengganti jumlah item tersebut
    try:
        order_items[nama_item][0] = update_jumlah_item
        
        print(f'Jumlah {nama_item.lower()} berhasil diubah!\n'
        f'Daftar barang yang Anda pesan adalah sebagai berikut: {order_items}')
    # Apabila tidak ada, menampilkan pesan kesalahan
    except KeyError as error:
        print(f'Pergantian jumlah {nama_item.lower()} gagal. {error}. Silakan coba lagi.')
```
---
**input_update_price()**<br>
`input_update_price()` meminta pelanggan memasukkan nama item yang harganya ingin diganti dan harga item yang baru secara berurutan.<br>
```
def input_update_price(order_items: dict):
    '''
    Fungsi untuk mengembalikan nama item yang harganya ingin diubah beserta harga yang baru
    args:
        order_items (dict): item yang telah dipesan beserta detailnya
    return:
        nama_item (str): nama item yang harganya ingin diubah
        update_harga_item (int): harga item yang baru
    '''
```
`nama_item` didapatkan dengan method `input_update()`.<br> 
`update_harga_item` didapatkan dengan method `input_int()`, dipastikan lebih dari 0 dan tidak sama dengan harga item sebelumnya.<br>
Terakhir, mengembalikan `nama_item` dan `update_harga_item`. 
```
    # Mengambil input nama dan harga item
    nama_item = input_update('Masukkan nama barang yang harganya ingin diupdate: ', order_items)
    update_harga_item = input_int(f'Masukkan harga {nama_item.lower()} yang baru: ')

    # Memastikan harga_item lebih dari 0
    while update_harga_item <= 0:
            print(f'Harga {nama_item} harus lebih dari 0. Silakan coba lagi.')
            update_harga_item = input_int(f'Masukkan harga {nama_item} yang baru: ')

    # Memastikan harga_item tidak sama dengan harga_item di dalam order_items
    while update_harga_item == order_items[nama_item][1]:
        print(f'Harga {nama_item.lower()} tidak boleh sama dengan sebelumnya: {order_items[nama_item][1]}')
        update_harga_item = input_int(f'Masukkan harga {nama_item.lower()} yang baru: ')
    
    return nama_item, update_harga_item
```
---
**update_item_price()**<br>
`update_item_price()` menerima `nama_item`, `update_harga_item`, dan `order_items` sebagai argumen, lalu mengganti harga `nama_item` di dalam `order_items` dengan `update_harga_item`.
```
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
```
Kode dijalankan dalam blok `try` dan `except` untuk menghandle `KeyError` apabila key `nama_item` tidak ditemukan di dalam `order_items`.<br>
Jika tidak ada error, mengassign value harga item pada key `nama_item` kepada `update_harga_item`.<br>
Jika ada error, menampilkan pesan kesalahan.
```
    # Memastikan nama_item ada di dalam order_items
    # Apabila ada, mengganti nama item tersebut
    try:
        order_items[update_nama_item] = order_items.pop(nama_item)

        print(f'{update_nama_item} berhasil ditambahkan!\n'
        f'Daftar barang yang Anda pesan adalah sebagai berikut: {order_items}')
    # Apabila tidak ada, menampilkan pesan kesalahan
    except KeyError as error:
        print(f'{update_nama_item} gagal ditambahkan. {error}. Silakan coba lagi.')
```
---
**input_delete()**<br>
`input_delete()` meminta pelanggan memasukkan nama item yang datanya ingin dihapus.
```
def input_delete(order_items: dict):
    '''
    Fungsi untuk mengembalikan nama item yang datanya ingin dihapus
    args:
        order_items (dict): item yang telah dipesan beserta detailnya
    return:
        nama item yang datanya ingin dihapus (str)
    '''
```
Langsung mengembalikan item yang didapatkan melalui method `input_update()`.
```
    return input_update('Masukkan nama barang yang ingin dihapus: ', order_items)
```
***delete_item()**<br>
`delete_item()` menerima `nama_item` dan `order_items` sebagai argumen, lalu menghapus data `nama_item` di dalam `order_items`.
```
def delete_item(nama_item: str, order_items: dict):
    '''
    Fungsi untuk menghapus data satu item
    args:
        nama_item (str): nama item yang ingin dihapus
        order_items (dict): item yang telah dipesan beserta detailnya
    return:
        None
    '''
```
Kode dijalankan dalam blok `try` dan `except` untuk menghandle `KeyError` apabila key `nama_item` tidak ditemukan di dalam `order_items`.<br>
Jika tidak ada error, menghapus data di dalam `order_items` dengan key `nama_item`.<br>
Jika ada error, menampilkan pesan kesalahan.
```
    # Memastikan nama_item ada di dalam order_items
    # Apabila ada, menghapus data item tersebut 
    try:
        order_items.pop(nama_item)

        print(f'{nama_item} berhasil dihapus!\n'
              f'Daftar barang yang Anda pesan adalah sebagai berikut: {order_items}')
    # Apabila tidak ada, menampilkan pesan kesalahan
    except KeyError as error:
        print(f'Penghapusan gagal. {error}. Silakan coba lagi.')
```
---
**reset_transaction()**<br>
`reset_transaction()` menerima `order_items` sebagai argumen lalu mengosongkan isinya.
```
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
```
---
**check_order()**
`check_order()` menerima `order_items` sebagai argumen lalu menampilkannya dalam bentuk tabel dengan bantuan modul `tabulate`.
```
from tabulate import tabulate

def check_order(order_items: dict):
    '''
    Fungsi untuk menampilkan daftar pesanan dalam bentuk tabulasi
    args:
        order_items (dict): item yang telah dipesan beserta detailnya
    return:
        table_items (dict): daftar pesanan dalam bentuk tabel
    '''
```
Pertama memeriksa apakah ada data yang missing dari `order_items` dan akan menampilkan pesan kesalahan apabila:
- ada key yang kosong
- ada jumlah atau harga item yang missing
- ada jumlah atau harga item yang bernilai 0 atau None
```
    # Menampilkan pesan kesalahan apabila terdapat data yang missing di dalam order_items
    for key, value in order_items.items():
        if key == '' or len(value) != 2 or 0 in value or None in value:
            print('Terdapat kesalahan dalam input data. Silakan coba lagi.')
            return
```
Jika tidak ada error, data di dalam `order_items` akan diubah menjadi `tabel_items` dengan kolom-kolom:
- No.
- Nama Item
- Jumlah Item
- Harga Item
- Total Harga (Harga Item dikalikan Jumlah Item)
```
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
```
Terakhir, menampilkan pesan tidak ada kesalahan dan `tabel_items` dalam bentuk tabel melalui `tabulate`, lalu mengembalikan `tabel_items`.
```
    # Menampilkan pesan tidak ada kesalahan dan tabulasi data pesanan
    print('Tidak ada kesalahan dalam input data. Silakan cek kembali pesanan Anda:')
    print(tabulate(table_items, headers='keys', tablefmt='grid'))

    return table_items
```
---
**check_out()**
`check_out()` menerima `table_items` sebagai argumen, lalu memasukkannya ke dalam SQLite database dengan bantuan method `insert_to_table()`.
```
def check_out(table_items: dict):
    '''
    Fungsi untuk menampilkan keseluruhan data pesanan dan memasukkannya ke dalam database
    args:
        table_items (dict): tabel data pesanan
    return:
        None
    '''
```
Sebelum data dimasukkan ke database, pelanggan akan menerima diskon sesuai ketentuan:
- 5% jika total harga per item lebih dari 200.000
- 6% jika total harga per item lebih dari 300.000
- 7% jika total harga per item lebih dari 500.000
Diskon dan harga setelah diskon yang diterima dimasukkan ke dalam list.
```
    diskon = []
    harga_diskon = []
```
Malakukan looping sesuai banyaknya item, lalu diskon tiap item dikalkulasi dan hasilnya dimasukkan ke dalam list.
```
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
```
List diskon dan harga setelah diskon dimasukkan ke dalam `table_items`.
```
    # Menambahkan list diskon dan harga setelah diskon ke dalam table_items
    table_items['Diskon'] = diskon
    table_items['Harga Setelah Diskon'] = harga_diskon
```
Menampilkan keseluruhan transaksi di `table_items` serta total pembayaran dari semua item.
```
    # Menampilkan tabulasi keseluruhan data pesanan dan total harga yang harus dibayarkan
    print(f'Detail transaksi Anda adalah sebagai berikut:')
    print(tabulate(table_items, headers='keys', tablefmt='grid'))
    print(f'Total pembayaran Anda adalah sebesar: {sum(harga_diskon)}')
```
Terakhir, memasukkan data di dalam `table_items` ke SQLite database melalui method `insert_to_table()`.
```
    # Mengeksekusi fungsi untuk memasukkan data ke dalam database
    insert_to_table(table_items)
```
---
**insert_to_table()**<br>
`insert_to_table()` menerima `table_items` sebagai argumen, lalu memasukkannya ke dalam SQLite database dengan bantuan modul `sqlalchemy`.<br>
Engine database dibuat terpisah di dalam modul `database_engine`.
```
from sqlalchemy import create_engine

# Membuat engine yang terhubung dengan database
def database_engine():
    '''
    Fungsi untuk membuat engine database
    args:
        None
    return:
        Fungsi untuk membuat engine database
    '''
    return create_engine('sqlite:///database/project.db', echo=True)
```
```
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
```
Membuat koneksi ke database dengan memanggil engine dan method `connect()`.
```
    # Membangun koneksi dengan database
    CONN = ENGINE().connect()
```
Membuat `insert_query` dengan bantuan method `text()` dari modul `sqlalchemy`.<br>
Data akan dimasukkan ke dalam tabel `items` dengan kolom-kolom:
- item_id (diomit di dalam query karena autoincrement)
- nama_item
- jumlah_item
- harga_item
- total_harga
- diskon
- harga_diskon

Masing-masing values ditandai dengan nama kolom masing-masing.
```
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
```
Kode dijalankan dalam blok `try` dan `except` untuk menghandle error yang terjadi pada saat query dieksekusi.<br>
Jika tidak ada error, melakukan looping pada list yang berada di dalam masing-masing kolom `table_items` dengan bantuan built-in `zip()`.
```
    try:
        # Mengakses data di list yang berada di masing-masing kolom tabel
        for (nama_item, jumlah_item, harga_item, total_harga, diskon, harga_diskon) in zip(
            table_items['Nama Item'],
            table_items['Jumlah Item'],
            table_items['Harga Item'],
            table_items['Total Harga'],
            table_items['Diskon'],
            table_items['Harga Setelah Diskon']):
```
Di dalam looping, melakukan eksekusi query dengan method `execute()` dengan argumen `insert_query` dan dictionary dengan:<br>
key: nama kolom tabel `items` yang telah digunakan untuk menandai values<br>
value: variabel yang menyimpan data dari `table_items`.
```
            # Mengeksekusi query
            CONN.execute(insert_query, {
                'nama_item': nama_item,
                'jumlah_item': jumlah_item,
                'harga_item': harga_item,
                'total_harga': total_harga,
                'diskon': diskon,
                'harga_diskon': harga_diskon
                })
```
Setelah looping selesai, melakukan `commit` untuk menyimpan perubahan di dalam database.
```
        # Melakukan commit untuk menyimpan perubahan di dalam database
        CONN.commit()
```
Jika ada error, menampilkan pesan kesalahan dan melakukan `rollback` untuk mengembalikan database ke keadaan semula.
```
    except Exception as error:
        print(error)

        # Apabila ada kesalahan, mengembalikan database ke keadaan semula
        CONN.rollback()
```
Menutup koneksi dengan database setelah semua task dikerjakan.
```
    # Menutup koneksi dengan database setelah semua task dikerjakan
    finally:
        CONN.close()
```
**PS:** Sebelum menjalankan `insert_to_table()`, tabel di dalam SQLite database telah dibuat dengan method `create_table()`.
```
def create_table():
    '''
    Fungsi untuk membuat tabel di dalam database
    args:
        None
    return:
        None
    '''
    # Membuat koneksi dengan database
    CONN = ENGINE().connect()

    # Membuat query untuk membuat tabel
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

    # Apabila tidak ada kesalahan, membuat tabel di dalam database
    try:
        # Mengeksekusi query
        CONN.execute(create_query)

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

create_table()
```
<br>

# Hasil Test Case
Test case dilakukan untuk memastikan fungsi-fungsi yang ditulis dapat bekerja dengan baik.

---
**Test Case 1:**
Pelanggan ingin menambahkan dua item baru dengan fungsi `add_item()`<br>
Item yang ditambahkan adalah sebagai berikut:
- Nama Item: Ayam Goreng, Qty: 2, Harga: 20000
- Nama Item: Pasta Gigi, Qty: 3, Harga: 15000
![Hasil test case 1](https://i.imgur.com/TPABcM1.png)

**Test Case 2:**
Pelanggan salah memasukkan salah satu item dari belanjaan, maka pelanggan ingin menghapusnya dengan fungsi `delete_item()`<br>
Item yang ingin dihapuskan adalah **Pasta Gigi.**
![Hasil test case 2](https://i.imgur.com/QtTJnu6.png)

**Test Case 3:**
Pelanggan salah memasukkan item yang ingin dibelanjakan. Daripada menghapus satu - satu, maka pelanggan ingin menghapus semua item yang sudah ditambahkan dengan fungsi `reset_transaction()`
![Hasil test case 3](https://i.imgur.com/GJchvUU.png)

**Test Case 4:**
Setelah pelanggan selesai menambahkan item kembali, ia ingin menghitung total belanja yang harus dibayarkan serta melihat item - item yang dibeli dengan fungsi `check_out()`<br>
1. Menginput ulang item berbeda
![Hasil test case 4](https://i.imgur.com/F17pe1y.png)
2. Melakukan check order dengan `check_order()`
![Hasil test case 4](https://i.imgur.com/hKsbbgf.png)
3. Melakukan check out dengan `check_out()`
![Hasil test case 4](https://i.imgur.com/JJckX2w.png)
4. Data telah masuk ke dalam tabel di SQLite database
![Hasil test case 4](https://i.imgur.com/qUEc9Ff.png)<br>
Isi tabel dapat dilihat dengan fungsi `select_table()`.
```
def select_table():
    '''
    Fungsi untuk melihat data tabel yang berada di dalam database
    args:
        None
    return:
        None
    '''
    # Membuat koneksi dengan database
    CONN = ENGINE().connect()

    # Membuat query untuk melihat data di dalam tabel
    select_query = text(
        """
        SELECT * FROM items
        """
    )

    # Mengeksekusi query
    table = CONN.execute(select_query)

    # Menampilkan tiap baris yang berada di dalam tabel
    for row in table:
            print(row)

    # Menutup koneksi dengan database setelah semua task dikerjakan
    CONN.close()
```
<br>

# Conclusion
Program Super Cashier adalah program yang dirancang untuk memasukkan input dari pelanggan dan secara otomatis memasukkannya ke dalam SQLite database.<br>
Hal-hal yang dapat dilakukan untuk memperbaiki program adalah:
1. Merefactor script menjadi script yang ditulis dalam bentuk Object Oriented Programming (OOP).
2. Menambahkan fitur tambahan seperti fitur yang menghandle pembayaran transaksi.