import unittest
import mytools


class TestMyTools(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(mytools.greet("Aisha"), "Hello Aisha")


if __name__ == "__main__":
    unittest.main()
