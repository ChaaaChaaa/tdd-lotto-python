from src.script.input import (
    print_input_manual_lotto_count,
    print_input_money,
    print_input_last_week_winner_numbers,
    print_input_bonus_number, print_input_manual_lotto_numbers,
)
from src.script.output import (
    print_lotto_numbers,
    print_reward,
    print_rate, print_buy_ticket,
)
from src.ticket.ticket import generate_auto_tickets, get_reward_ticket
from src.ticket.ticket_shop import buy_ticket
from src.utils.calculator import winner_ratio_calculator, calculate_auto_ticket_count


def get_user_inputs():
    input_money = print_input_money()
    manual_ticket_count = print_input_manual_lotto_count()
    manual_lotto_numbers = print_input_manual_lotto_numbers()

    # last_week_winner_numbers = print_input_last_week_winner_numbers()
    # bonus_number = print_input_bonus_number()
    return input_money, manual_ticket_count, manual_lotto_numbers


def get_rewards_inputs():
    last_week_winner_numbers = print_input_last_week_winner_numbers()
    bonus_number = print_input_bonus_number()
    return last_week_winner_numbers, bonus_number


def process_lotto(input_money, manual_ticket_count, manual_lotto_numbers,
                  ):
    count_ticket = buy_ticket(input_money)
    auto_ticket_count = calculate_auto_ticket_count(count_ticket,manual_ticket_count)
    print_buy_ticket(manual_ticket_count, auto_ticket_count)
    lotto_numbers = generate_auto_tickets(auto_ticket_count)
    print_lotto_numbers(lotto_numbers, manual_lotto_numbers)
    return lotto_numbers


def get_rewards_result(input_money, lotto_numbers, last_week_winner_numbers,
                       bonus_number):
    reward_counts = get_reward_ticket(bonus_number, last_week_winner_numbers,
                                      lotto_numbers)
    winner_ratio = winner_ratio_calculator(reward_counts, input_money)
    return reward_counts, winner_ratio


def display_results(reward_counts, winner_ratio):
    print_reward(reward_counts)
    print_rate(winner_ratio)


def main():
    input_money, manual_ticket_count, manual_lotto_numbers = get_user_inputs()

    lotto_numbers = process_lotto(input_money, manual_ticket_count,
                                  manual_lotto_numbers)
    last_week_winner_numbers, bonus_number = get_rewards_inputs()
    reward_counts, winner_ratio = get_rewards_result(input_money, lotto_numbers,
                                                     last_week_winner_numbers,
                                                     bonus_number)
    display_results(reward_counts, winner_ratio)


if __name__ == "__main__":
    main()
