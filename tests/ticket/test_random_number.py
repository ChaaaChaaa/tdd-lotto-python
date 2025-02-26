import unittest
from src.ticket.random_number import generate_random_numbers


class TestRandomNumber(unittest.TestCase):
    def test_get_random_number_length(self):
        numbers = generate_random_numbers()
        self.assertEqual(len(numbers), 6)

    def test_get_random_number_unique(self):
        numbers = generate_random_numbers()
        self.assertEqual(len(numbers), len(set(numbers)))

    def test_get_random_number_range(self):
        numbers = generate_random_numbers()
        for num in numbers:
            self.assertTrue(1 <= num <= 45)


if __name__ == '__main__':
    unittest.main()
