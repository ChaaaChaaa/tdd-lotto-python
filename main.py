from src.script.input import (
    get_input_money,
    print_input_last_week_winner_number,
    print_input_bonus_number,
)
from src.script.output import (
    print_buy_ticket,
    print_lotto_numbers,
    print_reward,
    print_rate,
)
from src.ticket.ticket import generate_tickets, get_reward_ticket
from src.ticket.ticket_shop import buy_ticket
from src.utils.calculator import winner_ratio_calculator


def get_user_inputs():
    input_money = get_input_money()
    last_week_winner_numbers = print_input_last_week_winner_number()
    bonus_number = print_input_bonus_number()
    return input_money, last_week_winner_numbers, bonus_number


def process_lotto(input_money, last_week_winner_numbers, bonus_number):
    count_ticket = buy_ticket(input_money)
    print_buy_ticket(count_ticket)
    lotto_numbers = generate_tickets(count_ticket)
    print_lotto_numbers(lotto_numbers)
    reward_counts = get_reward_ticket(bonus_number, last_week_winner_numbers,
                                      lotto_numbers)
    winner_ratio = winner_ratio_calculator(reward_counts, input_money)
    return reward_counts, winner_ratio


def display_results(reward_counts, winner_ratio):
    print_reward(reward_counts)
    print_rate(winner_ratio)


def main():
    input_money, last_week_winner_numbers, bonus_number = get_user_inputs()
    reward_counts, winner_ratio = process_lotto(input_money, last_week_winner_numbers,
                                                bonus_number)
    display_results(reward_counts, winner_ratio)


if __name__ == "__main__":
    main()
