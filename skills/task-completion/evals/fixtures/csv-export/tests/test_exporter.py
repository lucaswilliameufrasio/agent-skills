import unittest

from exporter import export_rows


class ExportTests(unittest.TestCase):
    def test_plain_rows(self):
        self.assertEqual(export_rows([["name", "role"]]), "name,role\n")


if __name__ == "__main__":
    unittest.main()
