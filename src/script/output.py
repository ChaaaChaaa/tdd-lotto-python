def print_buy_ticket(count_ticket):
    print(f"{count_ticket}개를 구매했습니다.")


def print_lotto_numbers(lotto_numbers):
    for lotto_number in lotto_numbers:
        print(lotto_number)


def print_reward(rewards):
    print("당첨 통계")
    print("---------")
    print("3개 일치 (5000원)- ", rewards[0], "개")
    print("4개 일치 (50000원)- ", rewards[1], "개")
    print("5개 일치 (1500000원)- ", rewards[2], "개")
    print("6개 일치 (2000000000원)- ", rewards[3], "개")


def print_rate(rate):
    if rate >= 1:
        print("총 수익률은 ", rate, "입니다.(기준이 1이기 때문에 결과적으로 이익라는 의미임)")
    else:
        print("총 수익률은 ", rate, "입니다.(기준이 1이기 때문에 결과적으로 손해라는 의미임)")
