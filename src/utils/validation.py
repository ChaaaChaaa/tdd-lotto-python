class Validation:

    @staticmethod
    def validate_empty_input(input):
        if input == '':
            print("값을 입력해 주세요.")
            return False
        return True
    
    @staticmethod
    def validate_input_number_range(input):
        if input<1 or input>45:
            print("1부터 45 사이의 숫자여야 합니다.")
            return False
        return True
    
    @staticmethod
    def validate_input_number_type(input):
        if not input.isdigit():
            return False
        return True
    
    @staticmethod
    def validate_input_number_length(input):
        if len(input) != 6:
            return False
        return True

    @staticmethod
    def validate_input_number_duplication(input):
        if len(input) != len(set(input)):
            return False
        return True
    
    @staticmethod
    def validate_input_money(input):
        if input<1000:
            return False
        return True

    @staticmethod
    def validate_last_week_winner_number(last_week_winner_number):
        for number in last_week_winner_number:
            if not Validation.validate_input_number_range(number):
                return False
            if not Validation.validate_input_number_type(number):
                return False
            if not Validation.validate_input_number_length(number):
                return False
            if not Validation.validate_input_number_duplication(number):
                return False
        return True
    

    
    @staticmethod
    def validate_bonus_number(bonus_number):
        if ',' in bonus_number:
            print("bonus number을 잘못 입력하셨습니다.")
            return False
        
        if not Validation.validate_empty_input(bonus_number):
            return False
        
        if not Validation.validate_input_number_type(bonus_number):
            print("bonus number은 숫자여야 합니다.")
            return False
        
        if not Validation.validate_input_number_range(bonus_number):
            return False        
        return True
    

    
