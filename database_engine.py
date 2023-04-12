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
    return create_engine(
    'sqlite:///C:/Users/LENOVO/OneDrive/Desktop/Engineering/Pacmann/'
    'Python/Projects/super-cashier/database/project.db', 
    echo=True
    )