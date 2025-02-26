import unittest
from unittest.mock import patch

from src.script.input import print_input_money, print_input_bonus_number, \
    print_input_last_week_winner_numbers, print_input_manual_lotto_numbers, \
    print_input_manual_lotto_count
import src.script.output as output
from src.ticket.ticket import get_reward_ticket
from src.ticket.ticket_shop import buy_ticket
from src.utils.calculator import winner_ratio_calculator, calculate_auto_ticket_count


class TestSimulation(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '10000',  # print_input_money() 호출
        '3',  # print_input_manual_lotto_count() 호출
        '8,21,23,41,42,43',  # print_input_manual_lotto_numbers() 내부 1번째 input()
        '3,5,11,16,32,38',  # print_input_manual_lotto_numbers() 내부 2번째 input()
        '7,11,16,35,36,44',  # print_input_manual_lotto_numbers() 내부 3번째 input()
        '',  # 종료를 위한 빈 문자열
        '1,2,3,4,5,7',  # print_input_last_week_winner_numbers() 호출
        '7'  # print_input_bonus_number() 호출
    ])
    @patch('src.ticket.ticket.random_number.generate_random_numbers',
           return_value=[1, 2, 3, 4, 5, 7])
    @patch('src.script.output.print_buy_ticket')
    @patch('src.script.output.print_lotto_numbers')
    @patch('src.script.output.print_reward')
    @patch('src.script.output.print_rate')
    def test_full_simulation(self, mock_print_rate, mock_print_reward,
                             mock_print_lotto_numbers, mock_print_buy_ticket,
                             mock_generate_random_numbers
                             ):
        # step1: 사용자 입력 - 구입금액
        input_money = print_input_money()
        self.assertEqual(input_money, 10000)

        # step2: 티켓구입 사용자 입력 - 수동
        count_ticket = buy_ticket(input_money)
        self.assertEqual(count_ticket, 10)

        manual_ticket_count = print_input_manual_lotto_count()
        self.assertEqual(manual_ticket_count, 3)

        manual_lotto_numbers = print_input_manual_lotto_numbers()
        self.assertEqual(manual_lotto_numbers,
                         [[8, 21, 23, 41, 42, 43],
                          [3, 5, 11, 16, 32, 38],
                          [7, 11, 16, 35, 36, 44]])

        auto_ticket_count = calculate_auto_ticket_count(count_ticket,
                                                        manual_ticket_count)

        self.assertEqual(auto_ticket_count, 7)

        # step2: 티켓 구입 - 자동
        count_ticket = buy_ticket(input_money)
        self.assertEqual(count_ticket, 10)
        output.print_buy_ticket(manual_ticket_count, auto_ticket_count)
        mock_print_buy_ticket.assert_called_once_with(manual_ticket_count,
                                                      auto_ticket_count)

        # Step3: 티켓 생성 (보너스 번호 포함)
        lotto_numbers = [mock_generate_random_numbers.return_value for _ in
                         range(count_ticket)]
        self.assertEqual(lotto_numbers[0], [1, 2, 3, 4, 5, 7])

        output.print_lotto_numbers(lotto_numbers, manual_lotto_numbers)
        mock_print_lotto_numbers.assert_called_once_with(lotto_numbers,
                                                         manual_lotto_numbers)

        # stpe4: 사용자 입력 - 지난 주 당첨 번호, 보너스 번호
        last_week_winner_numbers = print_input_last_week_winner_numbers()
        self.assertEqual(last_week_winner_numbers, [1, 2, 3, 4, 5, 7])

        bonus_number = print_input_bonus_number()
        self.assertEqual(bonus_number, 7)

        # step5: 보상 계산
        reward_counts = get_reward_ticket(bonus_number, last_week_winner_numbers,
                                          lotto_numbers)
        reward_ratio = winner_ratio_calculator(reward_counts, input_money)
        self.assertEqual(reward_counts[7], count_ticket)
        self.assertEqual(reward_ratio,
                         round(30000000.0 * count_ticket / input_money, 2))

        # step6: 보상 출력
        expected_rewards = [reward_counts.get(3, 0), reward_counts.get(4, 0),
                            reward_counts.get(5, 0), reward_counts.get(7, 0)]
        output.print_reward(expected_rewards)
        mock_print_reward.assert_called_once_with(expected_rewards)

        # step7: 수익률 출력
        output.print_rate(reward_ratio)
        mock_print_rate.assert_called_once_with(reward_ratio)

    if __name__ == '__main__':
        unittest.main()
