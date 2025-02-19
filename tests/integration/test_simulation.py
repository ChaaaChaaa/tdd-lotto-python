from itertools import cycle
import unittest
from unittest.mock import patch

from src.script.input import get_input_money, print_input_last_week_winner_number
import src.script.output as output
from src.ticket.ticket_shop import buy_ticket
from src.user.prize import prize_money


class TestSimulation(unittest.TestCase):
    @patch('builtins.input', side_effect=['5000', '1,2,3,4,5,6'])
    @patch('src.ticket.random_number.generate_random_numbers', side_effect=[
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6]
    ])
    @patch('src.script.output.print_buy_ticket')
    @patch('src.script.output.print_lotto_numbers')
    @patch('src.script.output.print_reward')
    @patch('src.script.output.print_rate')
    
    def test_full_simulation(self, mock_print_rate, mock_print_reward, mock_print_lotto_numbers, mock_print_buy_ticket, mock_generate_random_numbers, mock_input):
      #step1: 사용자 입력 - 구입금액
      input_money = get_input_money()
      self.assertEqual(input_money,5000)

      #step2: 티켓 구입
      count_ticket = buy_ticket(input_money)
      self.assertEqual(count_ticket,5)
      output.print_buy_ticket(count_ticket)
      mock_print_buy_ticket.assert_called_once_with(count_ticket)

     
      #stpe4: 사용자 입력 - 지난 주 당첨 번호
      last_week_winner_numbers = print_input_last_week_winner_number()
      self.assertEqual(last_week_winner_numbers,[1,2,3,4,5,6])

      #step5: 보상 계산
      reward_counts, reward_ratio = prize_money(input_money,count_ticket,last_week_winner_numbers)
      self.assertEqual(reward_counts[6],5)
      self.assertEqual(reward_ratio,2000000.0)

      #step6: 보상 출력
      output.print_reward([reward_counts.get(3,0), reward_counts.get(4,0), reward_counts.get(5,0), reward_counts.get(6,0)])
      expected_rewards = [0, 0, 0, 5]
      mock_print_reward.assert_called_once_with(expected_rewards)

      #step7: 수익률 출력
      output.print_rate(reward_ratio)
      mock_print_rate.assert_called_once_with(2000000.0)
    
    if __name__ == '__main__':
        unittest.main()