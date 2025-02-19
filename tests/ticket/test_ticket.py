import unittest
from unittest.mock import patch
from src.ticket.ticket import get_ticket, get_reward_ticket
from src.lotto.winner_number import get_last_week_winner_number

class TestTicket(unittest.TestCase):

    @patch('src.ticket.random_number.get_random_number', return_value=[1,2,3,4,5,6])
    def test_get_ticket(self, mock_get_random_number):
        tickets = get_ticket(3)
        self.assertEqual(tickets, [[1,2,3,4,5,6]] * 3)
        mock_get_random_number.assert_called_with()

    def test_get_reward_ticket(self):
        last_week_winners = [
            [1,2,3,4,5,6],
            [7,8,9,10,11,12]
        ]
        lotto_numbers = [
            [1,2,3,4,5,6],
            [7,8,9,10,11,12],
            [1,2,7,8,13,14]
        ]
        reward_counts = get_reward_ticket(last_week_winners, lotto_numbers)
        expected = {
            6: 1,
            6: 1,
            2: 1
        }
        # Since defaultdict with int, counts should accumulate
        self.assertEqual(reward_counts[6], 2)
        self.assertEqual(reward_counts[2], 1)

if __name__ == '__main__':
    unittest.main()
