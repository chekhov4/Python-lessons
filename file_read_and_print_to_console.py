def print_file_content(file_path):
    try:
        print_file = open(file_path, 'r')
    except IOError:
        print('File cannot be opened')
    else:
        print(print_file.read())
        print_file.close()

if __name__ == '__main__':
    file_path = 'c:\\temp\\test.txt'
    print_file_content(file_path)
