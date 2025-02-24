from src.utils.validation import Validation


def get_input_money():
    input_money = int(input("구입금액을 입력해 주세요. \n"))
    if Validation.validate_input_money(input_money):
        return input_money
    else:
        return get_input_money()


def print_input_last_week_winner_number():
    input_last_week_winner_number = input("지난 주 당첨 번호를 입력해 주세요. \n")
    last_week_winner_number = [int(num.strip()) for num in
                               input_last_week_winner_number.split(',')]
    if Validation.validate_last_week_winner_number(last_week_winner_number):
        return last_week_winner_number
    else:
        return print_input_last_week_winner_number()


def print_input_bonus_number():
    input_bonus_number = int(input("보너스 번호를 입력해 주세요. \n"))
    if Validation.validate_bonus_number(input_bonus_number):
        return input_bonus_number
    else:
        return print_input_bonus_number()
