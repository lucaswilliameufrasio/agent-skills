import unittest

from formatter import format_message


class FormatterTests(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(format_message("Ada"), "Hello, Ada!")


if __name__ == "__main__":
    unittest.main()
