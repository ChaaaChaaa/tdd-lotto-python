import unittest
from unittest.mock import patch
from src.script.input import print_input_money, print_input_last_week_winner_number


class TestInput(unittest.TestCase):
    @patch('builtins.input',return_value='5000')
    def test_print_input_money(self,mock_input):                
        input_money = print_input_money()
        self.assertEqual(input_money,5000)

    @patch('builtins.input',return_value='1,2,3,4,5,6')
    def test_print_input_last_week_winner_number(self,mock_input):
        last_week_winner_number = print_input_last_week_winner_number()
        self.assertEqual(last_week_winner_number,[1,2,3,4,5,6])

    @patch('builtins.input', return_value='1, 2, 3, 4, 5, 6')
    def test_print_input_last_week_winner_number_with_spaces(self, mock_input):
        last_week_winner_number = print_input_last_week_winner_number()
        self.assertEqual(last_week_winner_number,[1,2,3,4,5,6])

if __name__ == '__main__':
    unittest.main()