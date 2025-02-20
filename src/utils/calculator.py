from src.lotto.rewards import MatchCount


def calculate_prize_money(counts):
    prize_money = 0
    for money_count, ticket_count in counts.items():
        reward = MatchCount.get_reward(money_count)
        multiplied_reward = reward * ticket_count
        prize_money += multiplied_reward
    return prize_money


def winner_ratio_calculator(counts, input_money):
    if input_money == 0:
        return 0
    prize_money = calculate_prize_money(counts)
    winner_ratio = round(prize_money / input_money, 2)
    return winner_ratio
