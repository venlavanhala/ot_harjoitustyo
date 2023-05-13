
from entities.user import User
from repositories.note_repository import note_repository
from repositories.user_repository import user_repository

class InvalidCredentialsError(Exception):
    pass


class NoteFavors:
    """
    Luokka, joka vastaa sovelluslogiikasta
    """
    def __init__(self):
        self._user = None
        self._idnumber=None
        self._note_repository = note_repository
        self._user_repository = user_repository

    def sign_up(self, name, password):
        """Funktio, joka käsittelee rekisteröinnin

        Args:
            name
            password

        Returns:
        create: Uusi käyttäjäolio
        """
        check=self._user_repository.check_if_exist(name)
        if check is False or not check:
            create = self._user_repository.new_user(User(0, name, password))
            return create
        else:
            pass

    def current_user(self):
        """
        Funktio, joka palauttaa uuden käyttäjän
        Returns:
            self._user: Kirjautunut käyttäjä
        """
        return self._user

    def sign_in(self, name, password):
        """Funktio, joka hoitaa käyttäjän kirjautumisen

        Args:
            name: Käyttäjän nimi
            password: Käyttäjän salasana

        Returns:
            find: Kirjautunut käyttäjä
        """
        find=self._user_repository.find_user(name, password)
        if not find or find is None:
            raise InvalidCredentialsError("Käyttäjää ei löytynyt")
        self._user=find
        self._idnumber=self._user.idnumber
        return find

    def return_notes(self):
        """Funktio, joka palauttaa kirjoitetut muistiinpanot

        Returns:
            notes: Lista muistiinpanoista
        """
        notes=self._note_repository.all_notes(self._idnumber)
        if notes:
            return notes
        elif not notes or notes==None:
            return None

    def new_note(self, content):
        """Funktio, joka hoitaa muistiinpanojen tallennuksen

        Args:
            content: Muistiinpanon teksti
        """
        self._note_repository.new_note(self._idnumber, content)

notefavors=NoteFavors()
