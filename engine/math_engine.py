import math
from engine.exceptions import OutlandishError

def get_drama_level(value):
    """Calculates drama level based on magnitude brackets."""
    mag = abs(value)
    if mag < 10:
        return 1
    elif mag < 100:
        return 2
    elif mag < 1000:
        return 3
    elif mag < 10000:
        return 4
    else:
        return 5

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise OutlandishError("The universe cannot handle division by the void of zero!")
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        raise OutlandishError("The remainder of nothingness is a cosmic impossibility!")
    return a % b

def floor_divide(a, b):
    if b == 0:
        raise OutlandishError("Attempting to floor the infinite is a fool's errand!")
    return a // b

def root(a, b):
    if a < 0 and b % 2 == 0:
        raise OutlandishError("Imaginary numbers are too dramatic for this reality!")
    return a ** (1/b)