from database import get_db_connection

def create_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
