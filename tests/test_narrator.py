import pytest
from calculator.narrator import Narrator

def test_narrator_commentary_logic():
    narrator = Narrator()
    
    # Test Low Drama (0-3)
    assert narrator.get_commentary(10.0, 0) == "The result is 10.0."
    assert narrator.get_commentary(10.0, 3) == "The result is 10.0."
    
    # Test Medium Drama (4-7)
    assert narrator.get_commentary(10.0, 4) == "Quite interesting, the result is 10.0."
    assert narrator.get_commentary(10.0, 7) == "Quite interesting, the result is 10.0."
    
    # Test High Drama (8+)
    assert narrator.get_commentary(10.0, 8) == "UNBELIEVABLE! The result is 10.0!!!"
    assert narrator.get_commentary(10.0, 15) == "UNBELIEVABLE! The result is 10.0!!!"