BONUS_BALL = 1
NOT_BONUS_BALL = 0


def count_matching_numbers(last_week_winner_numbers, lotto_numbers,
                           bonus_number):
    match_count = len(set(last_week_winner_numbers) & set(lotto_numbers))
    is_bonus = match_count >= 5 and count_matching_bonus_number(bonus_number,
                                                                lotto_numbers)
    return match_count, BONUS_BALL if is_bonus else NOT_BONUS_BALL


def count_matching_bonus_number(bonus_number,
                                lotto_numbers):
    return bonus_number in lotto_numbers
