EASTER_EGGS = {
    42: "The answer to life, the universe, and everything.",
    666: "The number of the beast.",
    1337: "Elite status achieved.",
    80085: "Classic calculator humor.",
    0: "The void stares back.",
    7: "Lucky number seven!",
    101: "Back to basics.",
    9001: "It's over 9000!"
}

def check_easter_eggs(value: float) -> str:
    """Returns an easter egg message if the value matches, else None."""
    return EASTER_EGGS.get(value)