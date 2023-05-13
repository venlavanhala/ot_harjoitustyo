
class User:
    """Luokka, joka luo User-olion
    """
    def __init__(self, idnumber, name, password):
        """Luokan konstruktori

        Args:
            idnumber: id-numero
            name: Käyttäjän nimi
            password: Käyttäjän salasana
        """
        self.idnumber=idnumber
        self.name = name
        self.password = password
