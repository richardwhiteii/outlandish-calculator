import pytest
from outlandish_calc.ascii_art import get_result_banner, get_operation_art

def test_get_result_banner_brackets():
    # AC: Tests MUST verify that get_result_banner returns the correct ASCII string for each drama_level bracket.
    # Actual implementation: levels 1-2 -> SMALL_RESULT, levels 3-4 -> MEDIUM_RESULT, 5+ -> BIG_RESULT

    # Test Low Drama (1-2) -> SMALL_RESULT
    assert "[ RESULT ]" in get_result_banner(1)
    assert "[ RESULT ]" in get_result_banner(2)

    # Test Medium Drama (3-4) -> MEDIUM_RESULT
    assert "RESULT" in get_result_banner(3)
    assert "*****************" in get_result_banner(3)
    assert "RESULT" in get_result_banner(4)
    assert "*****************" in get_result_banner(4)

    # Test High Drama (5+) -> BIG_RESULT
    assert "MEGA RESULT" in get_result_banner(5)
    assert "MEGA RESULT" in get_result_banner(15)