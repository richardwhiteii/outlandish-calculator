import pytest
import math
from outlandish_calc.engine import calculate, CalcResult, OutlandishError, _get_drama_level


class TestBasicOperations:
    """Test all 8 supported operations."""

    def test_addition_integers(self):
        """Test addition with integers."""
        result = calculate('+', [10, 5])
        assert result.value == 15
        assert result.operation == '+'
        assert result.operands == [10, 5]
        assert isinstance(result, CalcResult)

    def test_addition_floats(self):
        """Test addition with floats."""
        result = calculate('+', [10.5, 4.5])
        assert result.value == pytest.approx(15.0)

    def test_addition_multiple_operands(self):
        """Test addition with multiple operands."""
        result = calculate('+', [1, 2, 3, 4])
        assert result.value == 10

    def test_subtraction(self):
        """Test subtraction."""
        result = calculate('-', [20, 7])
        assert result.value == 13
        assert result.operation == '-'

    def test_subtraction_floats(self):
        """Test subtraction with floats."""
        result = calculate('-', [20.0, 7.5])
        assert result.value == pytest.approx(12.5)

    def test_multiplication(self):
        """Test multiplication."""
        result = calculate('*', [6, 7])
        assert result.value == 42
        assert result.operation == '*'

    def test_multiplication_floats(self):
        """Test multiplication with floats."""
        result = calculate('*', [2.5, 4.0])
        assert result.value == pytest.approx(10.0)

    def test_division(self):
        """Test division."""
        result = calculate('/', [10, 2])
        assert result.value == pytest.approx(5.0)
        assert result.operation == '/'

    def test_division_floats(self):
        """Test division with floats."""
        result = calculate('/', [7.5, 2.5])
        assert result.value == pytest.approx(3.0)

    def test_power(self):
        """Test exponentiation."""
        result = calculate('**', [2, 3])
        assert result.value == 8
        assert result.operation == '**'

    def test_power_floats(self):
        """Test exponentiation with float exponent."""
        result = calculate('**', [4.0, 0.5])
        assert result.value == pytest.approx(2.0)

    def test_modulo(self):
        """Test modulo operation."""
        result = calculate('%', [10, 3])
        assert result.value == 1
        assert result.operation == '%'

    def test_modulo_floats(self):
        """Test modulo with floats."""
        result = calculate('%', [10.5, 4.0])
        assert result.value == pytest.approx(2.5)

    def test_sqrt(self):
        """Test square root."""
        result = calculate('sqrt', [16])
        assert result.value == pytest.approx(4.0)
        assert result.operation == 'sqrt'

    def test_sqrt_float(self):
        """Test square root with float."""
        result = calculate('sqrt', [2.0])
        assert result.value == pytest.approx(math.sqrt(2.0))

    def test_factorial(self):
        """Test factorial."""
        result = calculate('!', [5])
        assert result.value == 120.0
        assert result.operation == '!'

    def test_factorial_zero(self):
        """Test factorial of zero."""
        result = calculate('!', [0])
        assert result.value == 1.0


class TestErrorHandling:
    """Test error conditions and exception handling."""

    def test_division_by_zero(self):
        """Test that division by zero raises OutlandishError."""
        with pytest.raises(OutlandishError):
            calculate('/', [10, 0])

    def test_modulo_by_zero(self):
        """Test that modulo by zero raises OutlandishError."""
        with pytest.raises(OutlandishError):
            calculate('%', [10, 0])

    def test_sqrt_negative(self):
        """Test that sqrt of negative raises OutlandishError."""
        with pytest.raises(OutlandishError):
            calculate('sqrt', [-1])

    def test_factorial_negative(self):
        """Test that factorial of negative raises OutlandishError."""
        with pytest.raises(OutlandishError):
            calculate('!', [-1])

    def test_factorial_non_integer(self):
        """Test that factorial of non-integer raises OutlandishError."""
        with pytest.raises(OutlandishError):
            calculate('!', [3.5])

    def test_unsupported_operation(self):
        """Test that unsupported operation raises OutlandishError."""
        with pytest.raises(OutlandishError):
            calculate('&', [5, 3])

    def test_subtraction_missing_operand(self):
        """Test that subtraction with single operand raises OutlandishError."""
        with pytest.raises(OutlandishError):
            calculate('-', [5])

    def test_division_missing_operand(self):
        """Test that division with single operand raises OutlandishError."""
        with pytest.raises(OutlandishError):
            calculate('/', [5])


class TestDramaLevels:
    """Test drama level calculation based on result magnitude."""

    @pytest.mark.parametrize("value, expected_level", [
        (5, 1),          # < 10
        (9.9, 1),        # < 10
        (10, 2),         # 10-99
        (50, 2),         # 10-99
        (99, 2),         # 10-99
        (100, 3),        # 100-999
        (500, 3),        # 100-999
        (999, 3),        # 100-999
        (1000, 4),       # 1000-9999
        (5000, 4),       # 1000-9999
        (9999, 4),       # 1000-9999
        (10000, 5),      # >= 10000
        (50000, 5),      # >= 10000
        (-5, 1),         # Negative: < 10
        (-50, 2),        # Negative: 10-99
        (-500, 3),       # Negative: 100-999
        (-5000, 4),      # Negative: 1000-9999
        (-50000, 5),     # Negative: >= 10000
    ])
    def test_drama_level_brackets(self, value, expected_level):
        """Verify drama_level is correctly calculated across all magnitude brackets."""
        assert _get_drama_level(value) == expected_level

    def test_addition_drama_level(self):
        """Test that drama_level is correctly populated in CalcResult for addition."""
        result = calculate('+', [9, 1])  # Result: 10
        assert result.drama_level == 2

    def test_large_power_drama_level(self):
        """Test that large results get high drama levels."""
        result = calculate('**', [10, 5])  # Result: 100000
        assert result.drama_level == 5


class TestCalcResultFields:
    """Test that CalcResult populates all required fields."""

    def test_calc_result_has_all_fields(self):
        """Verify CalcResult contains all required fields."""
        result = calculate('+', [5, 3])
        assert hasattr(result, 'value')
        assert hasattr(result, 'operation')
        assert hasattr(result, 'operands')
        assert hasattr(result, 'drama_level')

    def test_operands_preserved(self):
        """Verify that operands are preserved in the result."""
        operands = [10, 20, 30]
        result = calculate('+', operands)
        assert result.operands == operands

    def test_operation_preserved(self):
        """Verify that operation string is preserved in the result."""
        result = calculate('*', [5, 4])
        assert result.operation == '*'

    def test_value_is_float(self):
        """Verify that value is returned as float."""
        result = calculate('+', [5, 3])
        assert isinstance(result.value, float)
        assert result.value == 8.0