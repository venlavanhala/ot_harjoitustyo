import unittest

from entities.user import User
from repositories.user_repository import UserTools


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user=User("Mikko", "kisu123")

    def test_printing(self):
        #person = User("Mikko", "kissa123")
        self.assertEqual(self.user.name, "Mikko")

    def test_check(self):
        #person = User("Mikko", "kissa123")
        #UserTools.check_if_exist("Mikko")
        self.assertEqual(UserTools.check_if_exist(self.user.name), "False")

    def test_new_user(self):
        #person=User("Mikko","kisu123")
        UserTools.new_user(self.user)
        self.assertEqual(self.user.name, "Mikko")