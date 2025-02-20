def get_input_money():
    input_money = int(input("구입금액을 입력해 주세요. \n"))
    return input_money


def print_input_last_week_winner_number():
    input_last_week_winner_number = input("지난 주 당첨 번호를 입력해 주세요. \n")
    last_week_winner_number = [int(num.strip()) for num in
                               input_last_week_winner_number.split(',')]
    return last_week_winner_number


def print_input_bonus_number():
    input_bonus_number = input("보너스 번호를 입력해 주세요. \n")
    bonus_number = input_bonus_number.strip()  # 숫자 하나만 받아야 하는데 그거 제한하기
    return int(bonus_number)
