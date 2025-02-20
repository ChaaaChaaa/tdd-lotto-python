# def get_last_week_winner_number(last_week_winner_numbers, lotto_numbers):
#     count = 0
#
#     for last_week_winner_number in last_week_winner_numbers.:
#         for number in last_week_winner_number:
#             if lotto_numbers in number:
#                 count+=1
#     return count

BONUS_BALL = 1
NOT_BONUS_BALL = 0


# def count_matching_numbers(last_week_winner_numbers, lotto_numbers,bonus_number): #set을 여기서 하는게 아닌거 같음 utils에서 해야하지 않을까
#     match_count = len(set(last_week_winner_numbers) & set(lotto_numbers))
#     if 5 >= match_count and count_matching_bonus_number(bonus_number,lotto_numbers):
#         return match_count,BONUS_BALL #true, false가 더 좋은까? 근데 그러면  count, bonus_count = count_matching_numbers(last_week_winner_numbers,~) 에서 복잡해질까봐, 그리고 count잖아 변수명이                                                  lotto_number, bonus_number)
#     return match_count,NOT_BONUS_BALL

def count_matching_numbers(last_week_winner_numbers, lotto_numbers,
                           bonus_number):  # set을 여기서 하는게 아닌거 같음 utils에서 해야하지 않을까
    match_count = len(set(last_week_winner_numbers) & set(lotto_numbers))
    is_bonus = match_count >= 5 and count_matching_bonus_number(bonus_number,
                                                                lotto_numbers)
    return match_count, BONUS_BALL if is_bonus else NOT_BONUS_BALL


def count_matching_bonus_number(bonus_number,
                                lotto_numbers):  # set을 여기서 하는게 아닌거 같음 utils에서 해야하지 않을까
    return bonus_number in lotto_numbers
