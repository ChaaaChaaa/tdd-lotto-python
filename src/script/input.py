def get_input_money():
    input_money = int(input("구입금액을 입력해 주세요. \n"))
    return input_money


def print_input_last_week_winner_number():
    input_last_week_winner_number = input("지난 주 당첨 번호를 입력해 주세요. \n")
    last_week_winner_number = [int(num.strip()) for num in
                               input_last_week_winner_number.split(',')]
    return last_week_winner_number
