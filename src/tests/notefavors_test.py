import unittest
from entities.user import User
from services.notefavors import notefavors

class FakeNoteRepository:
    def __init__(self, notes:None):
        self.notes = notes or []
        # [(0,"kisu"), (0,"koira"), (3,"haha")]

    def all_notes(self):
        return self.notes

    def return_notes(self, user_id):
        users_notes=[]
        for note in self.notes:
            if note[0]==user_id:
                users_notes.append(note[0])
        return users_notes

    def new_note(self, id, note):
        self.notes.append((id, note))
        return (id, note)

    def remove_notes(self):
        self.notes=[]


class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def all_users(self):
        return self.users

    def check_if_exist(self, name):
        for part in self.users:
            if name in part:
                return True
            else:
                return False
            
    def find_user(self, name, password):
        for user in users:
            # user=(1,"Venla", "kissa")
            if name in user and password in user:
                return User(user[0],user[1],user[2])

    def create(self, id, name, password):
        self.users.append((id, name, password))
        return User(id, name, password)

    def remove_users(self):
        self.users=[]

