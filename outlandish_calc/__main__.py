import re
import sys
import os
from outlandish_calc.engine import calculate, OutlandishError

# Import component modules
from outlandish_calc.narrator import Narrator
from outlandish_calc.ascii_art import get_result_banner, get_operation_art
from outlandish_calc.history import History
from outlandish_calc.easter_eggs import check_easter_egg

_narrator = Narrator()
_history = History()

BINARY_OPS = ('+', '-', '*', '/', '**', '%')

def parse_input(user_input: str):
    """
    Parse user input into (operation, operands) or return (None, None) for commands.

    Supported formats:
      - Infix binary: `2 + 3`, `10 - 4`, `2 ** 8`, `17 % 5`
      - sqrt:         `sqrt(144)` or `sqrt 144`
      - factorial:    `5!`

    Returns:
      (operation: str, operands: list[float])  on success
      Raises ValueError on malformed expressions.
    """
    s = user_input.strip()

    # factorial: `5!`
    factorial_match = re.fullmatch(r'(-?\d+(?:\.\d+)?)\s*!', s)
    if factorial_match:
        return ('!', [float(factorial_match.group(1))])

    # sqrt with parens: `sqrt(144)` or `sqrt( 144 )`
    sqrt_paren_match = re.fullmatch(r'sqrt\s*\(\s*(-?\d+(?:\.\d+)?)\s*\)', s, re.IGNORECASE)
    if sqrt_paren_match:
        return ('sqrt', [float(sqrt_paren_match.group(1))])

    # sqrt without parens: `sqrt 144`
    sqrt_space_match = re.fullmatch(r'sqrt\s+(-?\d+(?:\.\d+)?)', s, re.IGNORECASE)
    if sqrt_space_match:
        return ('sqrt', [float(sqrt_space_match.group(1))])

    # Infix binary: `<number> <op> <number>`
    # Try ** first (two-char operator), then single-char operators
    infix_match = re.fullmatch(
        r'(-?\d+(?:\.\d+)?)\s*(\*\*|[+\-*/%])\s*(-?\d+(?:\.\d+)?)',
        s
    )
    if infix_match:
        left = float(infix_match.group(1))
        op = infix_match.group(2)
        right = float(infix_match.group(3))
        return (op, [left, right])

    raise ValueError(f"Unrecognised expression: {s!r}")


def _show_stats():
    entries = _history.get_entries()
    print(f"Total calculations: {len(entries)}")


def main():
    """
    Main entry point for the Outlandish Calculator REPL.
    """
    print("Welcome to the Outlandish Calculator!")
    print("Type 'help' for usage, 'quit' or 'exit' to leave.")

    while True:
        try:
            try:
                user_input = input(">> ").strip()
            except EOFError:
                print("Farewell!")
                break

            if not user_input:
                continue

            lower = user_input.lower()

            # --- Commands ---
            if lower in ('quit', 'exit'):
                print("Farewell!")
                break

            if lower == 'help':
                print(
                    "Operations:\n"
                    "  2 + 3      addition\n"
                    "  10 - 4     subtraction\n"
                    "  3 * 7      multiplication\n"
                    "  15 / 3     division\n"
                    "  2 ** 8     exponentiation\n"
                    "  17 % 5     modulo\n"
                    "  sqrt(144)  square root\n"
                    "  5!         factorial\n"
                    "\nCommands: history, stats, clear, help, quit/exit"
                )
                continue

            if lower == 'history':
                entries = _history.get_entries()
                if entries:
                    for entry in entries:
                        print(entry)
                else:
                    print("No history yet.")
                continue

            if lower == 'stats':
                _show_stats()
                continue

            if lower == 'clear':
                clear_cmd = 'cls' if os.name == 'nt' else 'clear'
                os.system(clear_cmd)  # noqa: S605
                _history.clear()
                continue

            # --- Calculation ---
            try:
                operation, operands = parse_input(user_input)
                result = calculate(operation, operands)

                _history.add_entry(f"{user_input} = {result.value}")

                # Output sequence: operation art -> result banner -> narration -> easter egg
                op_art = get_operation_art(operation)
                if op_art:
                    print(op_art)
                print(get_result_banner(result.drama_level))
                print(_narrator.get_commentary(result.value, result.drama_level))
                egg = check_easter_egg(result.value)
                if egg:
                    print(egg)

            except ValueError as e:
                print(f"Invalid input: {e}")
            except OutlandishError as e:
                print(f"Calculation Error: {e}")

        except KeyboardInterrupt:
            print("\nI cannot be silenced!")
            sys.exit(0)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
