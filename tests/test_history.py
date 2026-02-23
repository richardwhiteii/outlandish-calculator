import pytest
from calculator.history import History

def test_history_eviction_at_limit():
    # AC: Tests MUST verify that History evicts the oldest record when the 101st calculation is added.
    history = History(max_size=100)
    # Add 100 items
    for i in range(100):
        history.add_entry(f"calc_{i}")
    
    assert len(history.get_entries()) == 100
    assert history.get_entries()[0] == "calc_0"
    
    # Add 101st item
    history.add_entry("calc_100")
    
    assert len(history.get_entries()) == 100
    assert history.get_entries()[0] == "calc_1"
    assert history.get_entries()[-1] == "calc_100"

def test_history_order_preserved():
    history = History()
    history.add_entry("first")
    history.add_entry("second")
    history.add_entry("third")
    
    assert history.get_entries() == ["first", "second", "third"]