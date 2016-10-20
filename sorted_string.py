def sort_string(test_string):

    if len(test_string) == 0:
        return ('Zero string')
    splitted_string = test_string.split(' ')
    splitted_string.sort(key = len)
    sorted_string =' '.join(splitted_string)


    return sorted_string