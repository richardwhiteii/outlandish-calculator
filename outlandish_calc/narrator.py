class Narrator:
    """A class that provides dramatic commentary on calculation results."""
    def get_commentary(self, result: float, drama_level: int) -> str:
        if drama_level <= 3:
            return f"The result is {result}."
        elif drama_level <= 7:
            return f"Quite interesting, the result is {result}."
        else:
            return f"UNBELIEVABLE! The result is {result}!!!"