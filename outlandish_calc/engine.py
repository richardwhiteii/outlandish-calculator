import math
from dataclasses import dataclass
from typing import List

class OutlandishError(Exception):
    """Custom exception for calculator errors."""
    pass

@dataclass
class CalcResult:
    """Data structure for calculation results."""
    value: float
    operation: str
    operands: List[float]
    drama_level: int

def _get_drama_level(value: float) -> int:
    """
    Calculates drama level based on magnitude thresholds.
    
    Thresholds:
    - Level 1: |value| < 10
    - Level 2: 10 <= |value| < 100
    - Level 3: 100 <= |value| < 1000
    - Level 4: 1000 <= |value| < 10000
    - Level 5: |value| >= 10000
    """
    magnitude = abs(value)
    if magnitude < 10:
        return 1
    if magnitude < 100:
        return 2
    if magnitude < 1000:
        return 3
    if magnitude < 10000:
        return 4
    return 5

def calculate(operation: str, operands: List[float]) -> CalcResult:
    """
    Performs the specified mathematical operation on the operands.
    
    Supported operations: +, -, *, /, **, %, sqrt, !
    
    Args:
        operation: The operator string.
        operands: List of numeric values.
        
    Returns:
        CalcResult object containing the result and metadata.
        
    Raises:
        OutlandishError: For invalid operations or mathematical errors.
    """
    try:
        if operation == '+':
            result = sum(operands)
        elif operation == '-':
            if len(operands) < 2:
                raise OutlandishError("Subtraction requires at least two operands.")
            result = operands[0] - operands[1]
        elif operation == '*':
            if len(operands) < 2:
                raise OutlandishError("Multiplication requires at least two operands.")
            result = operands[0] * operands[1]
        elif operation == '/':
            if len(operands) < 2:
                raise OutlandishError("Division requires at least two operands.")
            if operands[1] == 0:
                raise OutlandishError("Division by zero.")
            result = operands[0] / operands[1]
        elif operation == '**':
            if len(operands) < 2:
                raise OutlandishError("Power requires at least two operands.")
            result = operands[0] ** operands[1]
        elif operation == '%':
            if len(operands) < 2:
                raise OutlandishError("Modulo requires at least two operands.")
            if operands[1] == 0:
                raise OutlandishError("Division by zero.")
            result = operands[0] % operands[1]
        elif operation == 'sqrt':
            if len(operands) < 1:
                raise OutlandishError("Square root requires at least one operand.")
            if operands[0] < 0:
                raise OutlandishError("Square root of negative number.")
            result = math.sqrt(operands[0])
        elif operation == '!':
            if len(operands) < 1:
                raise OutlandishError("Factorial requires at least one operand.")
            val = operands[0]
            if val < 0:
                raise OutlandishError("Factorial of negative number.")
            if not float(val).is_integer():
                raise OutlandishError("Factorial of non-integer.")
            result = float(math.factorial(int(val)))
        else:
            raise OutlandishError(f"Unsupported operation: {operation}")

        return CalcResult(
            value=float(result),
            operation=operation,
            operands=operands,
            drama_level=_get_drama_level(result)
        )
    except (ZeroDivisionError, OverflowError, ValueError) as e:
        if isinstance(e, OutlandishError):
            raise e
        raise OutlandishError(str(e))