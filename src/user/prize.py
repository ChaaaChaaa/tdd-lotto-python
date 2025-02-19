from src.utils.calculator import winner_ratio_calculator
from src.lotto import winner_number, rewards
from src.ticket.ticket import generate_tickets, get_reward_ticket


def prize_money(input_money,tickets,last_week_winner_numbers):
    lotto_numbers = generate_tickets(tickets)
    reward_counts = get_reward_ticket(last_week_winner_numbers, lotto_numbers)
    reward_ratio = winner_ratio_calculator(reward_counts,input_money)
    return reward_counts,reward_ratio