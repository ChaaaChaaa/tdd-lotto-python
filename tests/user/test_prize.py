import unittest
from unittest.mock import patch
from src.user.prize import prize_money

class TestPrize(unittest.TestCase):

    @patch('src.ticket.ticket.get_ticket', return_value=[[1,2,3,4,5,6], [7,8,9,10,11,12]])
    @patch('src.ticket.ticket.get_reward_ticket', return_value={6:1, 6:1})
    @patch('src.utils.calculator.winner_ratio_calculator', return_value=2.0)
    def test_prize_money(self, mock_calculator, mock_get_reward_ticket, mock_get_ticket):
        input_money = 2000
        tickets = 2
        last_week_winners = [
            [1,2,3,4,5,6],
            [7,8,9,10,11,12]
        ]
        rewards, ratio = prize_money(input_money, tickets, last_week_winners)
        self.assertEqual(rewards, {6:1, 6:1})
        self.assertEqual(ratio, 2.0)
        mock_get_ticket.assert_called_with(tickets)
        mock_get_reward_ticket.assert_called_with(last_week_winners, [[1,2,3,4,5,6], [7,8,9,10,11,12]])
        mock_calculator.assert_called_with(input_money)

if __name__ == '__main__':
    unittest.main()
