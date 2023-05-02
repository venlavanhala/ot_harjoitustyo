from make_database import make_new_tables

def initialize():
    """
    Tämä metodi kutsuu tietokantataulujen poisto ja lisäysfunktioita kun ohjelmaa alustetaan.
    """
    make_new_tables()

if __name__ == "__main__":
    initialize()