'''
* 로또 구입 금액을 입력하면 구입 금액에 해당하는 로또를 발급해야 한다.
* 로또 1장의 가격은 1000원이다.
'''

TICKET_PRICE = 1000


def buy_ticket(input_money):
    count_ticket = input_money // TICKET_PRICE
    return count_ticket
