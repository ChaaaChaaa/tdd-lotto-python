import unittest
from unittest.mock import patch
from src.script.input import print_input_money, print_input_last_week_winner_numbers, \
    print_input_bonus_number, print_input_manual_lotto_count, \
    print_input_manual_lotto_numbers


class TestInput(unittest.TestCase):
    @patch('builtins.input', return_value='5000')
    def test_print_input_money(self, mock_input):
        input_money = print_input_money()
        self.assertEqual(input_money, 5000)

    @patch('builtins.input', return_value='1,2,3,4,5,6')
    def test_print_input_last_week_winner_number(self, mock_input):
        last_week_winner_number = print_input_last_week_winner_numbers()
        self.assertEqual(last_week_winner_number, [1, 2, 3, 4, 5, 6])

    @patch('builtins.input', return_value='1, 2, 3, 4, 5, 6')
    def test_print_input_last_week_winner_number_with_spaces(self, mock_input):
        last_week_winner_number = print_input_last_week_winner_numbers()
        self.assertEqual(last_week_winner_number, [1, 2, 3, 4, 5, 6])

    @patch('builtins.input', return_value='3')
    def test_print_input_bonus_number(self, mock_input):
        input_bonus_number = print_input_bonus_number()
        self.assertEqual(input_bonus_number, 3)

    @patch('builtins.input', return_value='2')
    def test_print_input_manual_lotto_count(self, mock_input):
        input_manual_lotto_count = print_input_manual_lotto_count()
        self.assertEqual(input_manual_lotto_count, 2)

    @patch('builtins.input', side_effect=['1,2,3,4,5,6', '1,2,3,7,8,9', ''])
    def test_print_input_manual_lotto_numbers(self, mock_input):
        input_manual_lotto_count = print_input_manual_lotto_numbers()
        self.assertEqual(input_manual_lotto_count,
                         [[1, 2, 3, 4, 5, 6], [1, 2, 3, 7, 8, 9]])


if __name__ == '__main__':
    unittest.main()
