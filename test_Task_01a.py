import unittest
from unittest.mock import patch
import Task_01a


class TestEchoProgram(unittest.TestCase):

    @patch('builtins.input', return_value='hello')
    @patch('builtins.print')
    def test_input_called(self, mock_print, mock_input):
        Task_01a.main()
        mock_input.assert_called()

    @patch('builtins.input', return_value='hello')
    @patch('builtins.print')
    def test_input_prompt(self, mock_print, mock_input):
        Task_01a.main()
        mock_input.assert_called_with('Shout: ')

    @patch('builtins.input', return_value='hello')
    @patch('builtins.print')
    def test_output_correct(self, mock_print, mock_input):
        Task_01a.main()
        mock_print.assert_called_with('hello hello hello')

if __name__ == '__main__':
    result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestEchoProgram))
    print(f'Tests run: {result.testsRun}')
    print(f'Failures: {len(result.failures)}')
    print(f'Errors: {len(result.errors)}')


