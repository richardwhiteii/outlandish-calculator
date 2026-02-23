import pytest
from calculator.ascii_art import get_result_banner

def test_get_result_banner_brackets():
    # AC: Tests MUST verify that get_result_banner returns the correct ASCII string for each drama_level bracket.
    
    # Test Low Drama (0-3)
    assert get_result_banner(0) == "[ RESULT ]"
    assert get_result_banner(3) == "[ RESULT ]"
    
    # Test Medium Drama (4-7)
    assert get_result_banner(4) == "=== RESULT ==="
    assert get_result_banner(7) == "=== RESULT ==="
    
    # Test High Drama (8+)
    assert get_result_banner(8) == "!!! *** RESULT *** !!!"
    assert get_result_banner(15) == "!!! *** RESULT *** !!!"