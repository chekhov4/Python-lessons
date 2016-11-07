def sort_file_strings(source_path, target_path):
    try:
        s_file = open(source_path, 'r+')
    except IOError:
        print('File cannot be opened')
        return

    file_strings = s_file.readlines()
    s_file.close()

    try:
        t_file = open(target_path, 'w')
    except IOError:
        print('Target file cannot be written')
        return

    for i in range(0, len(file_strings), 2):
        t_file.writelines(file_strings[i])
    t_file.close()



if __name__ == '__main__':

    file_path = 'c:\\temp\\test.txt'
    target_path = 'c:\\temp\\target.txt'
    sort_file_strings(file_path, target_path)
