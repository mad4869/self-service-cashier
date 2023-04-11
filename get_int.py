def get_int(prompt: str):
    '''
    Fungsi untuk menghandle Value Error saat menginput nilai integer
    args:
        prompt (str): prompt saat input data
    return:
        nilai integer yang dimasukkan user
    '''
    
    while True:
        # Mengembalikan nilai integer jika data yang dimasukkan benar
        try: 
            return int(input(prompt))
        # Menmberikan feedback apabila data yang dimasukkan bukan integer
        except ValueError as error:
            print(f'{error}. Mohon untuk memasukkan angka. Silakan coba lagi')