from entities.note import Note
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
        self._note_repository = note_repository
        self._user_repository = user_repository

    def sign_up(self, name, password):
        """Funktio, joka käsittelee rekisteröinnin

        Args:
            name
            password

        """
        check=self._user_repository.check_if_exist(name)
        if check==False:
            create = self._user_repository.new_user(User(name, password))
            return create
        else:
            raise InvalidCredentialsError("Käyttäjä on jo olemassa")

    def current_user(self):
        return self._user

    def sign_in(self, name, password):
        find=self._user_repository.find_user(name, password)
        if not find or find==None:
            raise InvalidCredentialsError("Käyttäjää ei löytynyt")
        self._user=find
        return find

    def return_notes(self, user):
        #if user!=self._user:
            #return []
        #else:
        notes=self._note_repository.all_notes(user)
        return list(notes)

    def new_note(self, content):
        note=Note(self._user.id, content)
        self._note_repository.new_note(note)
        return note

notefavors=NoteFavors()