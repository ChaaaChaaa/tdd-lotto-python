from src.lotto.winner_number import count_matching_numbers
from collections import defaultdict

from src.ticket import random_number

BONUS_REWARD_COUNT = 7


def get_reward_ticket(bonus_number, last_week_winner_numbers,
                      lotto_numbers):  # 변수가 3개인건 많지 않나
    reward_counts = defaultdict(int)

    for lotto_number in lotto_numbers:
        match_count, bonus_flag = count_matching_numbers(last_week_winner_numbers,
                                                         lotto_number, bonus_number)

        # if bonus_count >= 1:
        #     reward_counts[BONUS_REWARD_COUNT] += bonus_count
        # else:
        #     reward_counts[count] += 1 #depth가 3이라 바꿀필요있음
        key = BONUS_REWARD_COUNT if bonus_flag else match_count
        reward_counts[key] += 1

    for i in range(0, 7):
        if i not in reward_counts:
            reward_counts[i] = 0
    return reward_counts


def generate_tickets(count_ticket):
    # for i in range(len(tickets)):
    #     random_numbers = random_number.get_random_number()
    #     lotto_numbers.append(random_number
    lotto_numbers = [random_number.generate_random_numbers() for _ in
                     range(count_ticket)]
    return lotto_numbers
