def sort_file_strings(file_path):

    try:
        s_file = open(file_path, 'r+')
    except IOError:
        print('File cannot be opened')
        return

    file_strings = s_file.readlines()
    s_file.seek(0)
    s_file.writelines(sorted(file_strings, key = len))
    s_file.close()



if __name__ == '__main__':

    file_path = 'c:\\temp\\test.txt'
    sort_file_strings(file_path)
