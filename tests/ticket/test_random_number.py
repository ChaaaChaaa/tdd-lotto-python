import unittest
from src.ticket.random_number import get_random_number

class TestRandomNumber(unittest.TestCase):

    def test_get_random_number_length(self):
        numbers = get_random_number()
        self.assertEqual(len(numbers), 6)

    def test_get_random_number_unique(self):
        numbers = get_random_number()
        self.assertEqual(len(numbers), len(set(numbers)))

    def test_get_random_number_range(self):
        numbers = get_random_number()
        for num in numbers:
            self.assertTrue(1 <= num <= 45)

if __name__ == '__main__':
    unittest.main()
