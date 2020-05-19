from .algorithms import fibonacci, factorial, palindrome

def test_fibonacci_five():
    assert fibonacci(5) == 5

def test_palidrome_anita():
    assert palindrome('anita lava la tina')

def test_factorial_six():
    assert factorial(6) == 720