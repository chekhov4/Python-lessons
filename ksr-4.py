def delete_extra_spaces(source_string):
    words = source_string.split(' ')
    targer_string = ''
    double_space = False
    for word in words:
        if word == '' and double_space == True:
            continue
        if word == '':
            targer_string = targer_string + ' '
            double_space = True
            continue
            
        targer_string = targer_string + word
        double_space = False
    return targer_string


if __name__ == '__main__':
    source_string = ' 11   2  gfdfgdf '
    delete_extra_spaces(source_string)
