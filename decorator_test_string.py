
def wrapper(func):
    def check_function(*args, **kwargs):
        bracket = '{} [] ()'
        if len(source_string) < 2:
            print('String is too short')
            return 'String is too short'

        if len(bracket_type) != 2 or bracket.find(bracket_type) == -1:
            print('Wrong bracket set')
            return 'Wrong bracket set'

        if template == '':
            print('Template is empty')
            return 'Template is empty'

        if replace_all not in ['0','1']:
            print('Wrong substitution type')
            return 'Wrong substitution type'

        result = func(*args, **kwargs)
        return result
    return check_function



@wrapper
def subst_string(source_string, bracket_type, template, replace_all):
    result_string =''
    i = 0
    while i < len(source_string):

        if source_string[i] == bracket_type[0]:
            y = i + 1
            while source_string[y] != bracket_type[1]:
                y += 1

            if replace_all == '1':
                result_string += bracket_type[0] + template + bracket_type [1]
                i = y + 1
                continue

            else:
                result_string += bracket_type[0] + template + bracket_type [1]
                result_string += source_string[y + 1:]
                break

        result_string += source_string[i]
        i += 1


    return (result_string)


if __name__ == '__main__':
    source_string = raw_input('Input string ')
    bracket_type = raw_input('Input bracket type (), {}, []')
    template = raw_input('Inpunt substitution ')
    replace_all = raw_input('Input replacement type 0 - the fist mach, 1 - all ')
  

    print(subst_string(source_string, bracket_type, template, replace_all))



