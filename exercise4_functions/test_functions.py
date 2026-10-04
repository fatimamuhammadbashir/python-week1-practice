import unittest
from functions import greet


class TestFunctions(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("Aisha"), "Hello Aisha")


if __name__ == "__main__":
    unittest.main()
