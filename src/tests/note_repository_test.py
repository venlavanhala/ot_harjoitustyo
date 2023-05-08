import unittest
from repositories.note_repository import note_repository
from entities.note import Note


class TestNoteTools(unittest.TestCase):
    def setUp(self):
        note_repository.remove_notes()
        self.user_id=4
        self.content="Once upon a time"
        self.text="Olipa kerran elämä"

    def test_new_note(self):
        note_repository.new_note(self.user_id, self.text)
        all=note_repository.all_notes(self.user_id)
        self.assertEqual(len(all), 1)

    def test_all_notes(self):
        note_repository.new_note(self.user_id, self.text)
        note_repository.new_note(self.user_id, self.content)
        all=note_repository.all_notes(self.user_id)
        self.assertEqual(len(all), 2)