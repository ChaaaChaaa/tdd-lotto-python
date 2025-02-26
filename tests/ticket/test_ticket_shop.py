import unittest
from src.ticket.ticket_shop import buy_ticket


class TestTicketShop(unittest.TestCase):

    def test_buy_ticket_exact_amount(self):
        input_money = 5000
        count = buy_ticket(input_money)
        self.assertEqual(count, 5)

    def test_buy_ticket_non_exact_amount(self):
        input_money = 5500
        count = buy_ticket(input_money)
        self.assertEqual(count, 5)

    def test_buy_ticket_insufficient_amount(self):
        input_money = 999
        count = buy_ticket(input_money)
        self.assertEqual(count, 0)


if __name__ == '__main__':
    unittest.main()
