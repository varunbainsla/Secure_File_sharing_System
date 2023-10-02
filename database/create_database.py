import sqlite3


def create_table():
    conn = sqlite3.connect('user.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # # Define the SQL query to create the 'users' table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        user_id TEXT PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT UNIQUE,
        password TEXT,
        creation_datetime TEXT,
        is_active BOOLEAN,
        role TEXT
    );
    '''

    cursor.execute(create_table_query)

    print(cursor.fetchall())
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()
