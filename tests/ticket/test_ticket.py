import unittest
from unittest.mock import patch
from src.ticket.ticket import generate_auto_tickets, get_reward_ticket


class TestTicket(unittest.TestCase):

    @patch('src.ticket.random_number.generate_random_numbers',
           return_value=[1, 2, 3, 4, 5, 6])
    def test_get_ticket(self, mock_get_random_number):
        tickets = generate_auto_tickets(3)
        self.assertEqual(tickets, [[1, 2, 3, 4, 5, 6]] * 3)
        mock_get_random_number.assert_called_with()

    def test_get_reward_ticket_with_bonus(self):
        bonus_number = 13
        last_week_winners = [1, 2, 3, 4, 5, 6]
        lotto_numbers = [
            [1, 2, 3, 4, 5, 6],
            [7, 8, 9, 10, 11, 12],
            [1, 2, 3, 4, 5, 13]
        ]
        reward_counts = get_reward_ticket(bonus_number, last_week_winners,
                                          lotto_numbers)

        expected = {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1, 7: 1}

        self.assertEqual(reward_counts, expected)

    def test_get_reward_ticket(self):
        bonus_number = 7
        last_week_winners = [1, 2, 3, 4, 5, 6]
        lotto_numbers = [
            [1, 2, 3, 4, 5, 6],
            [7, 8, 9, 10, 11, 12],
            [1, 2, 7, 8, 13, 14]
        ]
        reward_counts = get_reward_ticket(bonus_number, last_week_winners,
                                          lotto_numbers)
        expected = {
            0: 1,
            1: 0,
            2: 1,
            3: 0,
            4: 0,
            5: 0,
            6: 1,
            7: 0
        }

        self.assertEqual(reward_counts, expected)


if __name__ == '__main__':
    unittest.main()
