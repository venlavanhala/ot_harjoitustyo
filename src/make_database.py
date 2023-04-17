from connect_database import get_database_connection


def remove_tables(db):
    cursor = db.cursor()

    cursor.execute("drop table if exists Users")
    cursor.execute("drop table if exists Notes")

    db.commit()


def create_tables(db):
    cursor = db.cursor()
    cursor.execute(
        "CREATE table Users (id integer primary key, name text, password text)")
    cursor.execute("CREATE table Notes (id integer primary key, " +
                   "user_id REFERENCES Users, day date, content text)")
    db.commit()

    db.commit()


def make_new_tables():
    db = get_database_connection()
    remove_tables(db)
    create_tables(db)
