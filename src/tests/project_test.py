import unittest

from entities.user import User

class TestUser(unittest.TestCase):
	def setUp(self):
		pass

	def test_printing(self):
		person=User("Mikko","kissa123")
		self.assertEqual(person.name, "Mikko")
