
from src.lotto.winner_number import count_matching_numbers
from collections import defaultdict

from src.ticket import random_number


def get_reward_ticket(last_week_winner_numbers, lotto_numbers):
    reward_counts = defaultdict(int)
    for lotto_number in lotto_numbers:
        count = count_matching_numbers(last_week_winner_numbers,
                                            lotto_number)
        reward_counts[count] += 1

    for i in range(0,7):
        if i not in reward_counts:
            reward_counts[i] = 0
    return reward_counts


def generate_tickets(count_ticket):
    # for i in range(len(tickets)):
    #     random_numbers = random_number.get_random_number()
    #     lotto_numbers.append(random_number
    lotto_numbers = [random_number.generate_random_numbers() for _ in range(count_ticket)]
    return lotto_numbers
