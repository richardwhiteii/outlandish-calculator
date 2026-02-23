import unittest
from unittest.mock import patch
import io
from calc.repl import repl_loop

class TestREPLIntegration(unittest.TestCase):
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_math_expression_dramatic_output(self, mock_stdout, mock_input):
        # Simulate entering a math expression then exiting
        mock_input.side_effect = ["5 + 5", "exit"]
        
        repl_loop()
        
        output = mock_stdout.getvalue()
        expected_sequence = (
            "--- DRAMATIC CALCULATION ---\n"
            "The numbers swirl in the void: 5 + 5\n"
            "The truth is revealed: 10\n"
            "----------------------------"
        )
        self.assertIn(expected_sequence, output)

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_history_command(self, mock_stdout, mock_input):
        # Simulate a calculation followed by the history command
        mock_input.side_effect = ["2 * 3", "history", "exit"]
        
        repl_loop()
        
        output = mock_stdout.getvalue()
        self.assertIn("=== CHRONICLES OF CALCULATION ===", output)
        self.assertIn("Replay: 2 * 3 = 6", output)

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_expression_error_narration(self, mock_stdout, mock_input):
        # Simulate an invalid expression (division by zero)
        mock_input.side_effect = ["1 / 0", "exit"]
        
        repl_loop()
        
        output = mock_stdout.getvalue()
        self.assertIn("!!! DRAMATIC ERROR !!!", output)
        self.assertIn("The heavens cry out:", output)

if __name__ == '__main__':
    unittest.main()