import unittest
from unittest.mock import patch
from io import StringIO

from gptclass import GPTClass
import textwrap


class GPTClassTest(unittest.TestCase):
    @patch("gptclass.function_utils.chat_completion")
    @patch("sys.stdout", new_callable=StringIO)
    def test_addition(self, stdout, chat_mock):
        chat_mock.return_value = textwrap.dedent(
            """
            ```python
            def add(a, b):
                return a+b
            ```
            """
        )
        gpt = GPTClass()
        self.assertEqual(gpt.add(4, 5), 9)
        self.assertEqual(gpt.add(2, 3), 5)
        self.assertEqual(stdout.getvalue(), "")  # No output expected

    @patch("gptclass.function_utils.chat_completion")
    @patch("sys.stdout", new_callable=StringIO)
    def test_explain_addition(self, stdout, chat_mock):
        chat_mock.return_value = textwrap.dedent(
            """
            ```python
            def add(a,b):
                return a+b
            ```
            """
        )
        gpt = GPTClass()
        gpt.explain.add(4, 5)
        self.assertEqual(stdout.getvalue(), "def add(a,b):\n    return a+b\n")

    @patch("gptclass.function_utils.chat_completion")
    def test_recursive_method(self, chat_mock):
        chat_mock.return_value = textwrap.dedent(
            """
            ```python
            def factorial(n):
                if n == 0:
                    return 1
                else:
                    return n * factorial(n-1)
            ```
            """
        )
        gpt = GPTClass()
        self.assertEqual(gpt.factorial(3), 6)
        self.assertEqual(gpt.factorial(7), 5040)

    @patch("gptclass.function_utils.chat_completion")
    def test_kwargs(self, chat_mock):
        chat_mock.return_value = textwrap.dedent(
            """
            ```python
            import random

            def random_plate_number(seed=None):
                random.seed(seed)
                letters = [chr(i) for i in range(65, 91)]
                plate_number = []
                for i in range(3):
                    plate_number.append(random.choice(letters))
                for i in range(4):
                    plate_number.append(str(random.randint(0,9)))
                return ''.join(plate_number)
            ```
            """
        )
        gpt = GPTClass()
        self.assertEqual(gpt.random_plate_number(seed=123), "BIC6410")

    @patch("gptclass.function_utils.chat_completion")
    def test_code_no_language(self, chat_mock):
        chat_mock.return_value = textwrap.dedent(
            """
            ```
            def f():
                return "hello!"
            ```
            """
        )
        gpt = GPTClass()
        self.assertEqual(gpt.f(), "hello!")
