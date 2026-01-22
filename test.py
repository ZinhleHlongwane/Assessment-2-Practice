"""
Assessment 2 Practice – Test File

This file tests the functions implemented in practice.py.

Instructions:
- Do NOT modify this file.
- Implement the functions in practice.py.
- Run this file to check your work.
"""

import practice

print("Running tests...\n")

# ================================
# CONDITIONAL STATEMENTS
# ================================

assert practice.check_even_or_odd(10) == "Even"
assert practice.check_even_or_odd(7) == "Odd"

assert practice.grade_classifier(85) == "Distinction"
assert practice.grade_classifier(65) == "Pass"
assert practice.grade_classifier(40) == "Fail"

print("✔ Conditional statements passed")


# ================================
# FUNCTIONS + BASIC LOOPS
# ================================

print("\nCount up from 1 to 5:")
practice.count_up(5)

print("\nCount down from 5 to 1:")
practice.count_down(5)

assert practice.sum_of_numbers(10) == 55

print("\nEven numbers up to 10:")
practice.print_even_numbers(10)

print("✔ Basic loops passed")


# ================================
# ADVANCED LOOPS
# ================================

print("\nFizz loop up to 15:")
practice.fizz_loop(15)

print("\nInput until stop (-1 to stop):")
count = practice.input_until_stop()
assert count >= 0

print("\nRunning total (0 to stop):")
practice.running_total()

print("\nBreak and continue logic:")
practice.break_and_continue_logic()

print("✔ Advanced loops passed")


# ================================
# PATTERNS / NESTED LOOPS
# ================================

square = practice.draw_star_square(3)
assert isinstance(square, str)
assert square.count("*") > 0

triangle = practice.right_aligned_triangle(4)
assert isinstance(triangle, str)

numbers = practice.number_pattern(4)
assert isinstance(numbers, str)

print("✔ Patterns passed")


# ================================
# SIMPLE ALGORITHMS
# ================================

assert practice.count_vowels("assessment") == 4
assert practice.is_prime(11) is True
assert practice.is_prime(12) is False
assert practice.factorial(5) == 120

print("✔ Simple algorithms passed")


# ================================
# CONDITIONAL + LOOPS
# ================================

print("\nPassword attempt test:")
practice.password_attempt()

print("\n🎉 All tests completed successfully!")
