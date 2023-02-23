import constants


def calculate_two_numbers(first_num, second_num, operator):
    match operator:
        case constants.ADD:
            return first_num + second_num
        
        case constants.SUB:
            return first_num - second_num
        
        case constants.DIV:
            return first_num / second_num
        
        case constants.MULT:
            return first_num * second_num
        
    raise Exception("Incorrect operation")    