def is_polindrom(source_string):
    polindrom = True
    for i in range(len(source_string) // 2):
        if source_string[i] != source_string[len(source_string) - 1 - i]:
            polindrom = False
            return polindrom

    return polindrom


if __name__ == '__main__':
    source_string = ' 1 1 '
    print (is_polindrom(source_string))
