from src.utils.validation import Validation


def print_input_money():
    input_money = input("구입금액을 입력해 주세요. \n")
    if Validation.validate_input_money(input_money):
        return int(input_money)
    else:
        return print_input_money()


def print_input_manual_lotto_count():
    input_manual_lotto_count = int(input("수동으로 구매할 로또 수를 입력해 주세요. \n"))
    if not Validation.validate_input_manual_lotto_count(input_manual_lotto_count):
        return input_manual_lotto_count
    else:
        return print_input_manual_lotto_count()


def print_input_manual_lotto_numbers():
    print("수동으로 구매할 번호를 입력해 주세요.")

    input_manual_lotto_numbers = list(iter(input, ""))  # input()이 빈 문자열을 반환할 때까지 호출
    manual_lotto_numbers_list = [
        [int(num.strip()) for num in line.split(',')]
        for line in input_manual_lotto_numbers if line.strip()
        # if line.strip() -> 내용있으면 True, 공백 또는 빈 줄 -> False
    ]
    if not all(Validation.validate_input_number_length(ticket) for ticket in
               manual_lotto_numbers_list):
        return print_input_manual_lotto_numbers()

    if not all(Validation.validate_numbers(num, ticket)
               for ticket in manual_lotto_numbers_list
               for num in ticket):
        return print_input_manual_lotto_numbers()

    return manual_lotto_numbers_list


def print_input_last_week_winner_numbers():
    input_last_week_winner_numbers = input("지난 주 당첨 번호를 입력해 주세요. \n")
    last_week_winner_numbers = [int(num.strip()) for num in
                                input_last_week_winner_numbers.split(',')]

    if not Validation.validate_input_number_length(last_week_winner_numbers):
        return print_input_last_week_winner_numbers()

    if not all(
            Validation.validate_numbers(number, last_week_winner_numbers) for number in
            last_week_winner_numbers):
        return print_input_last_week_winner_numbers()

    return last_week_winner_numbers


def print_input_bonus_number():
    input_bonus_number = int(input("보너스 번호를 입력해 주세요. \n"))
    if Validation.validate_bonus_number(input_bonus_number):
        return input_bonus_number
    else:
        return print_input_bonus_number()
