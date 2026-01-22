"""
Assessment 2 Practice – Test File

This file tests the functions implemented in main.py.

Instructions:
- Do NOT modify this file.
- Implement the functions in main.py.
- Run this file to check your work.
"""

import unittest
from io import StringIO
import sys

from main import (
    check_even_or_odd,
    grade_classifier,
    count_up,
    count_down,
    sum_of_numbers,
    print_even_numbers,
    fizz_loop,
    input_until_stop,
    running_total,
    break_and_continue_logic,
    draw_star_square,
    right_aligned_triangle,
    number_pattern,
    count_vowels,
    is_prime,
    factorial,
    password_attempt
)


class TestConditionals(unittest.TestCase):

    def test_even_or_odd(self):
        self.assertEqual(check_even_or_odd(4), "Even")
        self.assertEqual(check_even_or_odd(7), "Odd")

    def test_grade_classifier(self):
        self.assertEqual(grade_classifier(80), "Distinction")
        self.assertEqual(grade_classifier(65), "Pass")
        self.assertEqual(grade_classifier(40), "Fail")


class TestBasicLoops(unittest.TestCase):

    def capture_output(self, func, *args):
        captured = StringIO()
        sys.stdout = captured
        func(*args)
        sys.stdout = sys.__stdout__
        return captured.getvalue()

    def test_count_up(self):
        output = self.capture_output(count_up, 3)
        self.assertEqual(output, "1\n2\n3\n")

    def test_count_down(self):
        output = self.capture_output(count_down, 3)
        self.assertEqual(output, "3\n2\n1\n")

    def test_sum_of_numbers(self):
        self.assertEqual(sum_of_numbers(10), 55)

    def test_print_even_numbers(self):
        output = self.capture_output(print_even_numbers, 6)
        self.assertEqual(output, "2\n4\n6\n")


class TestAdvancedLoops(unittest.TestCase):

    def capture_output(self, func, *args):
        captured = StringIO()
        sys.stdout = captured
        func(*args)
        sys.stdout = sys.__stdout__
        return captured.getvalue()

    def test_fizz_loop(self):
        output = self.capture_output(fizz_loop, 5)
        expected = "1\n2\nFizz\n4\n5\n"
        self.assertEqual(output, expected)

    def test_input_until_stop(self):
        sys.stdin = StringIO("5\n3\n2\n-1\n")
        result = input_until_stop()
        sys.stdin = sys.__stdin__
        self.assertEqual(result, 3)

    def test_running_total(self):
        sys.stdin = StringIO("2\n3\n5\n0\n")
        output = self.capture_output(running_total)
        self.assertIn("10", output)

    def test_break_and_continue_logic(self):
        sys.stdin = StringIO("-5\n20\n150\n")
        output = self.capture_output(break_and_continue_logic)
        self.assertIn("20", output)


class TestPatterns(unittest.TestCase):

    def test_star_square(self):
        result = draw_star_square(3)
        expected = "***\n***\n***\n"
        self.assertEqual(result, expected)

    def test_right_aligned_triangle(self):
        result = right_aligned_triangle(3)
        expected = "  #\n ##\n###\n"
        self.assertEqual(result, expected)

    def test_number_pattern(self):
        result = number_pattern(4)
        expected = "1\n12\n123\n1234\n"
        self.assertEqual(result, expected)


class TestAlgorithms(unittest.TestCase):

    def test_count_vowels(self):
        self.assertEqual(count_vowels("assessment"), 4)
        self.assertEqual(count_vowels("sky"), 0)

    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(1))

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)


class TestPasswordAttempt(unittest.TestCase):

    def capture_output(self, func):
        captured = StringIO()
        sys.stdout = captured
        func()
        sys.stdout = sys.__stdout__
        return captured.getvalue()

    def test_password_success(self):
        sys.stdin = StringIO("secret\n")
        output = self.capture_output(password_attempt)
        self.assertIn("Access granted", output)

    def test_password_failure(self):
        sys.stdin = StringIO("a\nb\nc\n")
        output = self.capture_output(password_attempt)
        self.assertIn("Access denied", output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
