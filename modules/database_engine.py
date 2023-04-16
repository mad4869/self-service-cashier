from sqlalchemy import create_engine

# Membuat engine yang terhubung dengan database
def database_engine():
    '''
    Fungsi untuk mengembalikan objek engine database
    args:
        None
    return:
        Engine database (obj)
    '''
    return create_engine('sqlite:///../database/project.db', echo=True)