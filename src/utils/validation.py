class Validation:

    @staticmethod
    def validate_empty_input(input):
        if input == '':
            print("값을 입력해 주세요.")
            return False
        return True

    @staticmethod
    def validate_input_number_range(input):
        if int(input) < 1 or int(input) > 45:
            print("1부터 45 사이의 숫자여야 합니다.")
            return False
        return True

    @staticmethod
    def validate_input_number_type(input):
        input_number = str(input)
        if not input_number.isdigit():
            print("숫자여야 합니다.")
            return False
        return True

    @staticmethod
    def validate_input_range_money(input):
        money = int(input)

        if money != 0 or money < 1000:
            print("금액을 잘못적으셨습니다.")
            return False
        return True

    @staticmethod
    def validate_input_number_length(input_numbers):
        if len(input_numbers) != 6:
            print("로또 번호는 6개여야 합니다.")
            return False
        return True

    @staticmethod
    def validate_input_number_duplication(input_number, input_numbers):
        if input_numbers.count(input_number) > 1:
            print(f"로또 번호에 중복된 숫자가 있습니다. {input_number}")
            return False
        return True

    @staticmethod
    def validate_max_buy_lotto_count(max_lotto_count, manual_lotto_count):
        if manual_lotto_count > max_lotto_count:
            print("구매한 로또금액보다 많습니다.")
            return False
        return True

    @staticmethod
    def validate_input_money(input_money):
        if not Validation.validate_empty_input(input_money):
            return False
        if not Validation.validate_input_number_type(input_money):
            return False
        return True

    @staticmethod
    def validate_input_manual_lotto_count(input_manual_lotto_count):
        if not Validation.validate_input_number_type(input_manual_lotto_count):
            return False

    @staticmethod
    def validate_numbers(number, numbers):
        if not Validation.validate_input_number_range(number):
            return False
        if not Validation.validate_input_number_type(number):
            return False
        if not Validation.validate_input_number_duplication(number, numbers):
            return False
        return True

    @staticmethod
    def validate_bonus_number(bonus_number):
        if not Validation.validate_empty_input(bonus_number):
            return False

        if not Validation.validate_input_number_type(bonus_number):
            print("bonus number은 숫자여야 합니다.")
            return False

        if not Validation.validate_input_number_range(bonus_number):
            return False
        return True
