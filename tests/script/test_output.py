import unittest
from unittest.mock import patch
from src.script.output import print_buy_ticket, print_lotto_numbers, print_reward, \
    print_rate


class TestOutput(unittest.TestCase):

    @patch('builtins.print')
    def test_print_buy_ticket(self, mock_print):
        print_buy_ticket(3, 2)
        mock_print.assert_called_with("수동으로 3장, 자동으로 2장을 구매했습니다.")

    @patch('builtins.print')
    def test_print_lotto_numbers(self, mock_print):
        manual_lotto_numbers = [
            [13, 14, 15, 16, 17, 18],
            [1, 2, 3, 7, 8, 9],
            [1, 13, 14, 15, 19, 20]
        ]
        lotto_numbers = [
            [1, 2, 3, 4, 5, 6],
            [7, 8, 9, 10, 11, 12]
        ]
        print_lotto_numbers(lotto_numbers, manual_lotto_numbers)

        mock_print.assert_has_calls(
            [unittest.mock.call(manual_lotto_number) for manual_lotto_number in
             manual_lotto_numbers],
            [unittest.mock.call(lotto_number) for lotto_number in lotto_numbers],
        )

    @patch('builtins.print')
    def test_print_reward(self, mock_print):
        rewards = [0, 0, 0, 2, 1, 0, 0, 0]
        print_reward(rewards)
        expected_calls = [
            unittest.mock.call("당첨 통계"),
            unittest.mock.call("---------"),
            unittest.mock.call("3개 일치 (5000원)- ", 2, "개"),
            unittest.mock.call("4개 일치 (50000원)- ", 1, "개"),
            unittest.mock.call("5개 일치 (1500000원)- ", 0, "개"),
            unittest.mock.call("5개 일치, 보너스 볼 일치(30000000원)- ", 0, "개"),
            unittest.mock.call("6개 일치 (2000000000원)- ", 0, "개"),
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    def test_print_rate_profit(self, mock_print):
        print_rate(1.2)
        mock_print.assert_called_with("총 수익률은 ", 1.2,
                                      "입니다.(기준이 1이기 때문에 결과적으로 이익라는 의미임)")

    @patch('builtins.print')
    def test_print_rate_loss(self, mock_print):
        print_rate(0.8)
        mock_print.assert_called_with("총 수익률은 ", 0.8,
                                      "입니다.(기준이 1이기 때문에 결과적으로 손해라는 의미임)")


if __name__ == '__main__':
    unittest.main()
