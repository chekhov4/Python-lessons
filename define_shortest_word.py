def define_shortest_word(test_string):

    if len(test_string) == 0:
        return ('Zero string')
    splitted_string = test_string.split(' ')
    splitted_string.sort(key = len)

    for i in range(len(splitted_string)):

        sym = splitted_string[i]
        if sym.isalpha() == True:
            return len(sym)
    return ('no words in the string')