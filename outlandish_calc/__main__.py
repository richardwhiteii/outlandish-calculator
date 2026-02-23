import sys
import os
from outlandish_calc.engine import calculate, OutlandishError

# Import component modules
# These are assumed to be available in the environment as per the project structure
import outlandish_calc.display as display
import outlandish_calc.history as history
import outlandish_calc.stats as stats

def main():
    """
    Main entry point for the Outlandish Calculator REPL.
    """
    # Display welcome banner on startup
    display.print_welcome_banner()

    while True:
        try:
            # Prompt for input
            try:
                user_input = input(">> ").strip()
            except EOFError:
                # Handle Ctrl+D gracefully
                display.print_farewell_message()
                break

            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0].lower()
            args = parts[1:]

            # Handle exit commands
            if command in ('quit', 'exit'):
                display.print_farewell_message()
                break

            # Handle special commands
            if command == 'help':
                display.print_help()
                continue

            if command == 'history':
                history.print_history()
                continue

            if command == 'stats':
                stats.print_stats()
                continue

            if command == 'clear':
                # Clear the terminal screen
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

            # Attempt calculation
            try:
                # Parse operands
                operands = [float(arg) for arg in args]
                
                # Perform calculation
                result = calculate(command, operands)
                
                # Update history
                history.add_result(result)
                
                # Output sequence: ASCII Art -> Narration -> Easter Egg
                display.print_ascii_art(result)
                display.print_narration(result)
                display.print_easter_egg(result)

            except ValueError:
                # Failed to parse operands as floats
                print(f"Invalid input: Operands for '{command}' must be numbers.")
            except OutlandishError as e:
                # Engine error (e.g., division by zero)
                print(f"Calculation Error: {e}")

        except KeyboardInterrupt:
            # Catch Ctrl+C with dramatic message
            print("\nI cannot be silenced!")
            sys.exit(0)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()