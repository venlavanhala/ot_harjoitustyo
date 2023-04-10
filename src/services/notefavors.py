from entities.note import Note
from entities.user import User

from repositories.note_repository import NoteTools

from repositories.user_repository import UserTools

class NoteFavors:
    def __init__(self, note_repository, user_repository):
        self._user = None
        self._note_repository = note_repository
        self._user_repository = user_repository

    def sign_up(self, name, password):
        #tarkista ettei ole jo tätä käyttäjänimeä
        create=self._user_repository.new_user(User(name, password))
        return create
