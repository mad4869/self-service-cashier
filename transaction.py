import random

def transaction():
    '''
    Fungsi untuk men-generate nomor secara acak untuk digunakan sebagai id transaksi
    args:
        None
    return:
        id (int): nomor untuk id transaksi
    '''
    # Generate nomor secara acak
    id = random.randint(1, 10000)

    return id