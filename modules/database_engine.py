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
    return create_engine('sqlite:///../database/project.db', echo=True)