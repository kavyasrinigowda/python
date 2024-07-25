import unittest
from src.parser import parse_properties_file
from src.model import Model

class TestParser(unittest.TestCase):
    def setUp(self):
        self.model = Model('src/test/test_data/')
        self.properties = {
            'key1': 'value1'
        }

    def test_parse_properties_file(self):
        problems, missing_properties, new_properties = parse_properties_file(self.properties, self.model.xml_files)
        self.assertEqual(len(problems), 0)
        self.assertEqual(len(missing_properties), 0)
        self.assertEqual(len(new_properties), 0)

if __name__ == '__main__':
    unittest.main()
