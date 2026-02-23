import unittest
from unittest.mock import patch
import io
from outlandish_calc.__main__ import main as repl_loop

class TestREPLIntegration(unittest.TestCase):
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_math_expression_produces_output(self, mock_stdout, mock_input):
        # Simulate entering a math expression then exiting
        mock_input.side_effect = ["+ 5 5", "exit"]

        repl_loop()

        output = mock_stdout.getvalue()
        # Verify the REPL started and processed input without crashing
        self.assertIn("Welcome to the Outlandish Calculator!", output)
        self.assertIn("Farewell!", output)

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_history_command(self, mock_stdout, mock_input):
        # Simulate a calculation followed by the history command
        mock_input.side_effect = ["* 2 3", "history", "exit"]

        repl_loop()

        output = mock_stdout.getvalue()
        # History entries are stored and printed; verify no crash
        self.assertIn("Welcome to the Outlandish Calculator!", output)

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_operands_error_message(self, mock_stdout, mock_input):
        # Simulate invalid (non-numeric) operands
        mock_input.side_effect = ["+ abc def", "exit"]

        repl_loop()

        output = mock_stdout.getvalue()
        self.assertIn("Invalid input:", output)

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_exit_prints_farewell(self, mock_stdout, mock_input):
        mock_input.side_effect = ["exit"]

        repl_loop()

        output = mock_stdout.getvalue()
        self.assertIn("Farewell!", output)

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_eof_prints_farewell(self, mock_stdout, mock_input):
        mock_input.side_effect = EOFError

        repl_loop()

        output = mock_stdout.getvalue()
        self.assertIn("Farewell!", output)

if __name__ == '__main__':
    unittest.main()
