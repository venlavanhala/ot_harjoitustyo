import unittest
from repositories.user_repository import user_repository
from entities.user import User

class TestUserTools(unittest.TestCase):
    def setUp(self):
        user_repository.remove_users()
        self.liisa = User(0,"Liisa", "kisu")
        self.kerttu = User(0, "Kerttu", "koira")

    def test_new_user(self):
        user_repository.new_user(self.liisa)
        users = user_repository.all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0][1], self.liisa.name)

    def test_all_users(self):
        user_repository.new_user(self.liisa)
        user_repository.new_user(self.kerttu)
        users = user_repository.all_users()

        self.assertEqual(len(users), 2)

    def test_find_user(self):
        user_repository.new_user(self.liisa)

        user = user_repository.find_user(self.liisa.name, self.liisa.password)

        self.assertEqual(user.name, self.liisa.name)
        self.assertEqual(user.idnumber, 1)
