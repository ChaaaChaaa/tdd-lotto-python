from src.lotto.rewards import MatchCount
import math


def winner_ratio_calculator(counts, input_money):
    prize_money = 0

    for money_count, ticket_count in counts.items():
        reward = MatchCount.get_reward(money_count)
        prize_money += reward*ticket_count # prize_money += reward 에서 수정

    if input_money == 0:
        return 0

    winner_ratio = math.floor((prize_money / input_money) * 10) / 10
    return winner_ratio
