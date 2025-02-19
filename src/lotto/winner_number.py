# def get_last_week_winner_number(last_week_winner_numbers, lotto_numbers):
#     count = 0
#
#     for last_week_winner_number in last_week_winner_numbers.:
#         for number in last_week_winner_number:
#             if lotto_numbers in number:
#                 count+=1
#     return count


def count_matching_numbers(last_week_winner_numbers, lotto_numbers):
    return len(set(last_week_winner_numbers) & set(lotto_numbers))