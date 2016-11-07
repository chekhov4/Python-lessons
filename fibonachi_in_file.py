def write_number_of_fibonachi(number_of_fibonachi, path_to_file):
    fibonachi_row = []
    fibonachi_prev = 1
    for i in range (1, number_of_fibonachi):
        fibonachi_new = i * fibonachi_prev
        fibonachi_row.append(fibonachi_new)
        fibonachi_prev = fibonachi_new

    fibonachi_file = open(path_to_file, 'w')
    fibonachi_file.write(str(fibonachi_row))
    fibonachi_file.close()


if __name__ == '__main__':

    number_of_fibonachi = 7
    path_to_file = 'c:\\temp\\fibonachi.txt'
    write_number_of_fibonachi(number_of_fibonachi, path_to_file)