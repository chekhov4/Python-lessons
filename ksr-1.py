def check_value(value):
    if value % 3 == 0 and value % 10 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    value = 20
    check_value(value)
    
