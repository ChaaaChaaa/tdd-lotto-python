import src.script.output
from src.ticket.ticket import generate_tickets, get_reward_ticket
from src.ticket.ticket_shop import buy_ticket
from src.user.prize import prize_money, winner_ratio_calculator
from src.script.input import get_input_money, print_input_last_week_winner_number
from src.script.output import print_buy_ticket, print_lotto_numbers, print_reward


def main():
    input_money = get_input_money()
    count_ticket = buy_ticket(input_money)
    print_buy_ticket(count_ticket)

    lotto_numbers = generate_tickets(count_ticket)
    print_lotto_numbers(lotto_numbers)

    last_week_winner_numbers = print_input_last_week_winner_number()
    reward_counts = get_reward_ticket(last_week_winner_numbers, lotto_numbers)

    winner_ratio = prize_money(reward_counts,input_money)
    src.script.output.print_rate(winner_ratio)


if __name__ == "__main__":
    main()
