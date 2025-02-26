import unittest
from src.lotto.winner_number import count_matching_numbers


class TestWinnerNumber(unittest.TestCase):

    def test_count_matching_numbers(self):
        last_week_winners = [1, 2, 3, 4, 5, 6]

        lotto_numbers = [1, 2, 7, 8, 13, 14]
        count = count_matching_numbers(last_week_winners, lotto_numbers,
                                       bonus_number=13)
        self.assertEqual(count, (2, 0))

        lotto_numbers = [13, 14, 15, 16, 17, 18]
        count = count_matching_numbers(last_week_winners, lotto_numbers,
                                       bonus_number=13)
        self.assertEqual(count, (0, 0))


if __name__ == '__main__':
    unittest.main()
