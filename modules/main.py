# BACKGROUND

# Andi adalah PEMILIK SUPERMARKET BESAR
# Ia ingin membuat SISTEM KASIR SELF-SERVICE
# Customer bisa langsung:
    # - MEMASUKKAN ITEM
    # - JUMLAH ITEM
    # - HARGA ITEM


# CUSTOMER JOURNEY

# 1. Customer memasukkan NAMA ITEM, JUMLAH ITEM, HARGA BARANG
    # >>> Dimasukkan ke dalam LIST sebagai PARAM dari FUNCTION
    # add_item([<nama item>, <jumlah item>, <harga per item>])
from inputs import input_item
from add_item import add_item

nama_items, jumlah_items, harga_items = input_item()

order_items = add_item(nama_items, jumlah_items, harga_items)

# 2. Customer dapat melakukan UPDATE DATA
    # >>> UPDATE NAMA ITEM dengan FUNCTION update_nama_item(<nama item>, <update nama>)
    # >>> UPDATE JUMLAH ITEM dengan FUNCTION update_jumlah_item(<nama item>, <update jumlah>)
    # >>> UPDATE HARGA ITEM dengan FUNCTION update_harga_item(<nama item>, <update harga>)
from inputs import input_update_name
from update_item import update_item_name

nama_item, nama_item_baru = input_update_name(order_items)
update_item_name(nama_item, nama_item_baru, order_items)

from inputs import input_update_qty
from update_item import update_item_qty

nama_item, jumlah_item = input_update_qty(order_items)
update_item_qty(nama_item, jumlah_item, order_items)

from inputs import input_update_price
from update_item import update_item_price

nama_item, harga_item = input_update_price(order_items)
update_item_price(nama_item, harga_item, order_items)

# 3. Customer dapat MEMBATALKAN TRANSAKSI
    # >>> MENGHAPUS ITEM dengan FUNCTION delete_item(<nama_item>)
    # >>> MENGHAPUS SEMUA TRANSAKSI dengan FUNCTION reset_transaction()
from inputs import input_delete
from delete_item import delete_item

nama_item = input_delete(order_items)

delete_item(nama_item, order_items)

from delete_item import reset_transaction

reset_transaction(order_items)

# 4. Customer dapat MEMERIKSA ULANG PESANAN
    # >>> Menggunakan FUNCTION check_order()
        # >>> Mengeluarkan pesan PEMESANAN SUDAH BENAR apabila TIDAK ADA KESALAHAN INPUT
        # >>> Mengeluarkan pesan TERDAPAT KESALAHAN INPUT apabila ADA KESALAHAN INPUT
            # >>> Mengeluarkan OUTPUT TRANSAKSI
                # >>> Terdiri dari NOMOR, NAMA ITEM, JUMLAH ITEM, HARGA/ITEM, TOTAL HARGA
from check_order import check_order

table_items = check_order(order_items)

# 5. Customer dapat MENGHITUNG TOTAL BELANJA
    # >>> Menggunakan FUNCTION check_out()
        # >>> Jika TOTAL > 200_000 -> DISKON 5%
        # >>> Jika TOTAL > 300_000 -> DISKON 6%
        # >>> Jika TOTAL > 500_000 -> DISKON 7%
    # >>> Jika check_out() dijalankan -> DATA TRANSAKSI dimasukkan ke SQLITE DATABASE pada 
    # TABEL TRANSACTION menggunakan FUNCTION insert_to_table(<source_data>)
        # >>> Kolom yang disimpan:
            # i. no_id (auto increment)
            # ii. nama_item
            # iii. jumlah_item
            # iv. harga
            # v. total_harga
            # vi. diskon
            # vii. harga_diskon
from check_out import check_out

check_out(table_items)

# 6. Memastikan item telah masuk ke dalam database
    # >>> Menggunakan FUNCTION select_table()

from select_table import select_table

select_table()