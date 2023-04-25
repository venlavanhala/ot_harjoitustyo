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
        #person = User("Mikko", "kissa123")
        self.assertEqual(self.user.name, "Mikko")

    def test_check(self):
        #person = User("Mikko", "kissa123")
        #UserTools.check_if_exist("Mikko")
        self.assertEqual(self.tools.check_if_exist(self.user.name), None)

    def test_new_user(self):
        testi=NoteTools.new_user(self.liisa)
        self.assertEqual(testi, self.liisa)

    def test_making_note(self):
        testi=self.favor.new_note("kissa")
        self.assertEqual(testi[1], "kissa")
