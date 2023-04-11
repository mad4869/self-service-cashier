# Super Cashier
Super Cashier adalah program berbasis python yang dirancang agar seorang pelanggan dapat memasukkan sendiri item serta jumlah dan harga item ke dalam daftar pesanan yang kemudian akan disimpan di dalam SQLite database.

# Background
Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia. Andi memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu membuat sistem kasir self-service di supermarket miliknya dengan harapan:
- Customer bisa langsung memasukkan item, jumlah item, dan harga item yang dibeli serta beberapa fitur lain.
- Customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut.

# Requirements
Beberapa fitur program yang dibutuhkan pada Super Cashier antara lain:
1. Pelanggan dapat membuat ID transaksi
2. Pelanggan dapat memasukkan nama, jumlah, dan harga item ke dalam daftar pesanan
3. Pelanggan dapat memperbarui nama, jumlah, dan harga item yang telah dimasukkan sebelumnya
4. Pelanggan dapat menghapus salah satu atau seluruh item dari daftar pesanan
5. Pelanggan dapat memeriksa ulang daftar pesanan yang telah dibuat
6. Pelanggan dapat melihat total pembayaran dari keseluruhan transaksi

# Alur Program
![A flowchart image that explains how the program runs](https://lh3.googleusercontent.com/pw/AJFCJaXlFgkPPfIle8mwsIyh7ro7IRY3UiYjJFC-GFwkQk6g_afzNOjt_57LEOIlf0zlMfp7IHRfwjsO0yieq3DnYS-HQF98j3eTwfLcyj6dGvn4zrwcHubVI3uZEou2VIEMnZiFCRWdcOSJACHWR4tO3q-bgvZCxgoLTYrda2YrDf3QVSoyKdlQcSD7GQQhD1WnnFfTSKb5QBuStiU_eu9LIr-zM8lCIqTCY_FBiUWYi32r4vKmj7WX4mJ-i-VYGb3QHWFF7H5QJt9uyJODwNX7WVpIjXmuhIXO8N2CeMyfTbCjrl5vIS2AMyYSrq6ekF-VloKrJPZ8PiCbfAcL3WVWCxttDqCHwv-I-qwkQ0appFmJhIWTHOr0sDsu-CE6Fd8boZBKdQ1-UUzp6nmI2OxBm-xi5yA9hgy7sBLyhjLGgQi9HX7eDbESfceE5UdV5WggIKsC1iCfdAZgIiFpS37d-oIPkuhT6cHJRCZHn3vJ14Gi6N44RLL0rWbWgUGEphmbHZcUGsP_TWE2gNVtnmwI3OYT_DbVjkuuU-UvPbfvwdqio3rES8yxyx8lFwYsc_n5Mv2K0Ysr1X23owuH5YFIcFyDhJo3LvQxi-K30tq6MXpI4ZNf2kDQHCIePtbH8qdTuPZDszsSjvtHrsWOzrYYk8Dw0gG_NsOuialZI9E50XITstH8VldHC4jvGls9Zf5y4DEhzEfPv0hRP4d-rvSPH5YZrPniW4O2XWCjsMIISG37Hg5hA2R8iptDf8MFnKV_w_KizS31kKreU6p10BwSD76FH4GGV7i_CFpPHdr3Vm5TDC4WBwL1ALxdYST29q5TPkvujhk4vrbdYL1o5DQr5TdWUzvnphGYj4WAMhGNVGqpCDUPMDkQf98h-l7H7pWklLuzm0akh-N03iO7VRPciQ=w1920-h698-s-no?authuser=0)

# Penjelasan Code

# Hasil Test Case
1. Pelanggan ingin menambahkan dua item baru. Item yang ditambahkan adalah sebagai berikut:
- Nama Item: Ayam Goreng, Qty: 2, Harga: 20000
- Nama Item: Pasta Gigi, Qty: 3, Harga: 15000

2. Ternyata pelanggan salah memasukkan salah satu item dari belanjaan, maka pelanggan ingin menghapusnya. Item yang ingin dihapuskan adalah Pasta Gigi.

3. Ternyata pelanggan salah memasukkan item yang ingin dibelanjakan! Daripada menghapus satu - satu, maka pelanggan ini menghapus semua item yang sudah ditambahkan.

4. Setelah pelanggan selesai menambahkan item, ia ingin menghitung total belanja yang harus dibayarkan serta melihat item - item yang dibeli.
