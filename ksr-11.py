def find_string_in_file(file_path, search_string):
    count_maches = 0
    with open(file_path, 'r') as source_file:
        file_content = source_file.readlines()
    source_file.close()

    for string in file_content:
        if string[0:-1] == search_string:
            count_maches += 1

    return count_maches

if __name__ == '__main__':
    search_string = 'hey hey'
    file_path = 'c:\\temp\\test.txt'
    find_string_in_file(file_path, search_string)
