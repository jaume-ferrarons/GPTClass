import unittest
from unittest.mock import patch
from io import StringIO

from gptclass import GPTClass


class GPTClassTest(unittest.TestCase):
    def test_addition(self):
        gpt = GPTClass()
        self.assertEqual(gpt.add(4, 5), 9)
        self.assertEqual(gpt.add(2, 3), 5)

    @patch("sys.stdout", new_callable=StringIO)
    def test_explain_addition(self, stdout):
        gpt = GPTClass()
        gpt.explain.add(4, 5)
        self.assertEqual(stdout.getvalue(), "def add(a, b):\n    return a + b\n")

    def test_recursive_method(self):
        gpt = GPTClass()
        self.assertEqual(gpt.factorial(3), 6)
        self.assertEqual(gpt.factorial(7), 5040)
