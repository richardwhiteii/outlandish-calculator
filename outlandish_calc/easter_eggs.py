import math
from typing import Optional

def check_easter_egg(value: float) -> Optional[str]:
    """
    Checks if a calculated value matches a 'magic' number and returns a dramatic message.
    
    Triggers:
    - Infinity: "To infinity and beyond!"
    - 42: "The answer to life, the universe, and everything."
    - 69: "Nice."
    - 404: "Error: Result not found (just kidding)."
    - 666: "The number of the beast!"
    - pi: "Mmm... pie." (Tolerance: 0.001)
    - 0: "The void stares back."
    - Negative: "A bit negative, aren't we?"
    
    Args:
        value: The numeric result to check.
        
    Returns:
        A string message if a trigger is met, otherwise None.
    """
    if math.isinf(value):
        return "To infinity and beyond!"
    
    if value == 42:
        return "The answer to life, the universe, and everything."
    
    if value == 69:
        return "Nice."
    
    if value == 404:
        return "Error: Result not found (just kidding)."
    
    if value == 666:
        return "The number of the beast!"
    
    if math.isclose(value, math.pi, abs_tol=0.001):
        return "Mmm... pie."
    
    if value == 0:
        return "The void stares back."
    
    if value < 0:
        return "A bit negative, aren't we?"
    
    return None