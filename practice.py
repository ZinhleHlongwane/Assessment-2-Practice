# ================================
# CONDITIONAL STATEMENTS
# ================================

def check_even_or_odd(n: int) -> str:
    """
    Determine whether a number is even or odd.

    Args:
        n (int): An integer.

    Returns:
        str: "Even" if the number is even, otherwise "Odd".
    """
    pass


def grade_classifier(score: int) -> str:
    """
    Classify a score into a grade.

    Rules:
        75+  -> "Distinction"
        60–74 -> "Pass"
        Below 60 -> "Fail"

    Args:
        score (int): Student score (0–100).

    Returns:
        str: Grade classification.
    """
    pass


# ================================
# FUNCTIONS + BASIC LOOPS
# ================================

def count_up(n: int) -> None:
    """
    Print all numbers from 1 to n, each on a new line.

    Args:
        n (int): A positive integer.

    Returns:
        None
    """
    pass


def count_down(n: int) -> None:
    """
    Print all numbers from n down to 1.

    Args:
        n (int): A positive integer.

    Returns:
        None
    """
    pass


def sum_of_numbers(n: int) -> int:
    """
    Calculate the sum of all numbers from 1 to n using a loop.

    Args:
        n (int): A positive integer.

    Returns:
        int: The sum from 1 to n.
    """
    pass


def print_even_numbers(n: int) -> None:
    """
    Print only the even numbers between 1 and n.

    Args:
        n (int): A positive integer.

    Returns:
        None
    """
    pass


# ================================
# ADVANCED LOOPS
# ================================

def fizz_loop(n: int) -> None:
    """
    Print numbers from 1 to n using a loop.

    - Print "Fizz" if the number is divisible by 3
    - Otherwise print the number

    Args:
        n (int): A positive integer.

    Returns:
        None
    """
    pass


def input_until_stop() -> int:
    """
    Continuously ask the user to enter numbers.
    Stop when the user enters -1.
    Count how many numbers were entered (excluding -1).

    Returns:
        int: Number of values entered before -1.
    """
    pass


def running_total() -> None:
    """
    Continuously ask the user for numbers.
    After each input, print the running total.
    Stop when the user enters 0.

    Returns:
        None
    """
    pass


def break_and_continue_logic() -> None:
    """
    Ask the user to enter numbers repeatedly.

    - Skip negative numbers
    - Stop the loop if the number is greater than 100
    - Print all valid numbers

    Returns:
        None
    """
    pass


# ================================
# PATTERNS / NESTED LOOPS
# ================================

def draw_star_square(n: int) -> str:
    """
    Draw a square made of '*' characters.

    Args:
        n (int): Number of rows and columns.

    Returns:
        str: A string representation of the square.
    """
    pass


def right_aligned_triangle(n: int) -> str:
    """
    Draw a right-aligned triangle of '#' characters.

    Args:
        n (int): Height of the triangle.

    Returns:
        str: A string representation of the triangle.
    """
    pass


def number_pattern(n: int) -> str:
    """
    Print a number pattern using nested loops.

    Example for n = 4:
        1
        12
        123
        1234

    Args:
        n (int): Height of the pattern.

    Returns:
        str: A string representation of the pattern.
    """
    pass


# ================================
# SIMPLE ALGORITHMS / PROBLEM-SOLVING
# ================================

def count_vowels(word: str) -> int:
    """
    Count how many vowels appear in a given word.

    Args:
        word (str): Input word.

    Returns:
        int: Number of vowels in the word.
    """
    pass


def is_prime(n: int) -> bool:
    """
    Determine whether a number is prime using a loop.

    Args:
        n (int): A positive integer.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    pass


def factorial(n: int) -> int:
    """
    Calculate the factorial of a number using a loop.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: n factorial (n!)
    """
    pass


# ================================
# CONDITIONAL + LOOPS
# ================================

def password_attempt() -> None:
    """
    Give the user 3 attempts to enter the correct password.

    - If correct → print "Access granted"
    - If incorrect after 3 attempts → print "Access denied"

    Returns:
        None
    """
    pass


# ================================
# BASIC COMMAND LINE (CONCEPTUAL)
# ================================

def command_line_practice() -> None:
    """
    Write down (do NOT code) the command-line commands for:

    1. Showing the current directory
    2. Listing files in a directory
    3. Creating a new directory called 'projects'
    4. Changing into the 'projects' directory
    5. Creating a file called 'test.py'
    6. Running a Python file from the terminal

    (Practice these in your terminal, not in Python.)
    """
    pass
