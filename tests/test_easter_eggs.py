import pytest
from calculator.easter_eggs import check_easter_eggs

@pytest.mark.parametrize("value, expected", [
    (42, "The answer to life, the universe, and everything."),
    (666, "The number of the beast."),
    (1337, "Elite status achieved."),
    (80085, "Classic calculator humor."),
    (0, "The void stares back."),
    (7, "Lucky number seven!"),
    (101, "Back to basics."),
    (9001, "It's over 9000!")
])
def test_easter_egg_triggers(value, expected):
    # AC: Tests MUST verify that all 8 easter eggs trigger correctly with their respective values.
    assert check_easter_eggs(value) == expected

def test_no_easter_egg():
    assert check_easter_eggs(123.45) is None