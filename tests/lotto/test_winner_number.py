import unittest
from src.lotto.winner_number import get_last_week_winner_number

class TestWinnerNumber(unittest.TestCase):

    def test_get_last_week_winner_number(self):
        last_week_winners = [
            [1, 2, 3, 4, 5, 6],
            [7, 8, 9, 10, 11, 12]
        ]
        lotto_numbers = [1, 2, 7, 8, 13, 14]
        count = get_last_week_winner_number(last_week_winners, lotto_numbers)
        self.assertEqual(count, 4)

        lotto_numbers = [13, 14, 15, 16, 17, 18]
        count = get_last_week_winner_number(last_week_winners, lotto_numbers)
        self.assertEqual(count, 0)

if __name__ == '__main__':
    unittest.main()
        