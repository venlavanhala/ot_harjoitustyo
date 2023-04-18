from connect_database import get_database_connection


def remove_tables(database):
    cursor = database.cursor()

    cursor.execute("drop table if exists Users")
    cursor.execute("drop table if exists Notes")

    database.commit()


def create_tables(database):
    cursor = database.cursor()
    cursor.execute(
        "CREATE table Users (id integer primary key, name text, password text)")
    cursor.execute("CREATE table Notes (id integer primary key, " +
                   "user_id REFERENCES Users, day date, content text)")
    database.commit()

    database.commit()


def make_new_tables():
    database = get_database_connection()
    remove_tables(database)
    create_tables(database)
