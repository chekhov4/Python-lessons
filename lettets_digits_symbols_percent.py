def calc_percent(test_string):
"""
calculate % of digits, letters and special symbols in the string
"""
    total_digit = 0
    total_letter = 0
    total_special_char = 0
    if len(test_string) == 0:
        return ('Zero string')

    for i in range(len(test_string)):
        sym = test_string[i]
        if sym.isdigit() == True:
            total_digit += 1
        elif sym.isalpha() == True:
            total_letter += 1
        else:
            total_special_char +=1

    digit_percent = total_digit * 100 / len(test_string)
    letter_percent = total_letter * 100 / len(test_string)
    special_char_percent = total_special_char * 100 / len(test_string)

    return (digit_percent, letter_percent, special_char_percent)