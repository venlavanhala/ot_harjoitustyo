import unittest

from entities.user import User
from entities.note import Note
from repositories.user_repository import UserTools
from repositories.note_repository import NoteTools

class TestUserTools(unittest.TestCase):
    def setUp(self):
        self.liisa=User("Liisa","kissa")
        self.kerttu=User("Kerttu", "koira")

    def test_printing(self):
        person = User("Mikko", "kissa123")
        self.assertEqual(person.name, "Mikko")

    def test_check(self):
        #person = User("Mikko", "kissa123")
        #UserTools.check_if_exist("Mikko")
        self.assertEqual(UserTools.check_if_exist(self.liisa.name), None)

    def test_new_user(self):
        UserTools.new_user(self.liisa)
        testi=UserTools.all_users()
        self.assertEqual(len(testi), 1)

    #def test_making_note(self):
        #testi=self.favor.new_note("kissa")
        #self.assertEqual(testi[2], "kissa")
