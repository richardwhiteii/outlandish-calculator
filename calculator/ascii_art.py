def get_result_banner(drama_level: int) -> str:
    """
    Returns an ASCII banner based on the drama level.
    Brackets:
    0-3: Simple
    4-7: Decorative
    8+: Explosive
    """
    if drama_level <= 3:
        return "[ RESULT ]"
    elif drama_level <= 7:
        return "=== RESULT ==="
    else:
        return "!!! *** RESULT *** !!!"