import unittest
from src.utils.calculator import winner_ratio_calculator
from src.lotto.rewards import MatchCount

class TestCalculator(unittest.TestCase):

    def test_winner_ratio_calculator(self):
        counts = {3:2, 4:1, 5:0, 6:1}
        input_money = 5000
        expected_prize_money = (MatchCount.get_reward(3) * 2) + (MatchCount.get_reward(4) * 1) + (MatchCount.get_reward(6) * 1)
        expected_ratio = (expected_prize_money / input_money)
        expected_ratio = (expected_prize_money / input_money)
        expected_ratio = (expected_prize_money / input_money)
        expected_ratio = (expected_prize_money / input_money)
        rounded_ratio = expected_ratio  # floor was used in original code
        self.assertEqual(winner_ratio_calculator(counts, input_money), rounded_ratio)

    def test_winner_ratio_calculator_zero_input_money(self):
        counts = {3:2, 4:1}
        input_money = 0
        with self.assertRaises(ZeroDivisionError):
            winner_ratio_calculator(counts, input_money)

    def test_winner_ratio_calculator_no_rewards(self):
        counts = {}
        input_money = 1000
        expected_ratio = 0
        self.assertEqual(winner_ratio_calculator(counts, input_money), expected_ratio)

if __name__ == '__main__':
    unittest.main()
