import unittest
from src.model import Model

class TestModel(unittest.TestCase):
    def test_load_xml_files(self):
        model = Model('src/test/test_data/')
        self.assertGreater(len(model.xml_files), 0)  # Ensure XML files are loaded

if __name__ == '__main__':
    unittest.main()
