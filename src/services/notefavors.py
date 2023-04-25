from entities.note import Note
from entities.user import User

from repositories.note_repository import NoteTools
from repositories.user_repository import UserTools


class NoteFavors:
    def __init__(self):
        self._user = None
        self._note_repository = NoteTools
        self._user_repository = UserTools

    def sign_up(self, name, password):
        check=self._user_repository.check_if_exist(name)
        if check!="False":
            create = self._user_repository.new_user(User(name, password))
            return create

    def current_user(self):
        return self._user

    def sign_in(self, name, password):
        find=self._user_repository.find_user(name, password)
        if find!="None":
            self._user=find

    def return_notes(self, user):
        if not self._user:
            return []
        else:
            notes=self._note_repository.all_notes(user)
            return list(notes)

    def new_note(self, content):
        note=Note(self._user, content)
        NoteTools.new_note(note)
        return note