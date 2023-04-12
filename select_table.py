from sqlalchemy import text
from database_engine import engine as ENGINE

def select_table():
    CONN = ENGINE().connect()

    select_query = text(
        """
        SELECT * FROM items
        """
    )

    table = CONN.execute(select_query)
    for row in table:
            print(row)

    CONN.close()