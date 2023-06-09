from connect_database import get_database_connection


def remove_tables(database):
    """
    Poistaa tietokantataulut
    """
    cursor = database.cursor()

    cursor.execute("drop table if exists Users")
    cursor.execute("drop table if exists Notes")

    database.commit()


def create_tables(database):
    """
    Luo uudet tietokantataulut
    """
    cursor = database.cursor()
    cursor.execute("CREATE table Users (id integer primary key, name text, password text)")
    cursor.execute("CREATE table Notes (id integer primary key, user_id integer REFERENCES " +
                   "Users(id), content text)")
    database.commit()


def make_new_tables():
    """
    Poistaa ja luo taulut
    """
    database = get_database_connection()
    remove_tables(database)
    create_tables(database)

if __name__=="__main__":
    make_new_tables()
