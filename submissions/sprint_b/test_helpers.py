import os
import json
import unittest

from .helpers import FileManager, Vocabulary, EpithetGenerator

path = os.getenv("JSON_FILE_PATH")


class FileManagerTest(unittest.TestCase):
    """Test for the FileManager class in helpers.py"""

    def test_get_extension(self):
        self.assertEqual(FileManager.get_extension(path), "json")

    def test_read_json(self):
        with open(os.path.abspath(path)) as file:
            self.assertEqual(json.loads(file.read()), FileManager.read_json(
                os.path.abspath(path)))

    def test_read_json_sad(self):
        with self.assertRaises(FileNotFoundError):
            FileManager.read_json("/randompath")


class VocabularyTest(unittest.TestCase):
    """Test for the Vocabulary class in helpers.py"""

    def test_from_file_sad_path(self):
        with self.assertRaises(KeyError):
            Vocabulary.from_file('')

    def test_junk_path(self):
        with self.assertRaises(FileNotFoundError):
            Vocabulary.from_file('/stuff.json')

    def test_json_return(self):
        with open(os.path.abspath(path)) as f:
            data = json.load(f)
            representation = (data, data.keys())
            self.assertEqual(representation, Vocabulary.from_json(path))
