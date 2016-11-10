def update_account_file(client_name, account_change):
    import random
    dict_client_balance = {}
    dict_client_acc_number = {}
    client_file_path = 'c:\\temp\\acc_file.txt'

    try:
        account_file = open(client_file_path, 'r')
    except IOError:
        account_file = open(client_file_path, 'w')
    finally:
        account_file.close()

    with open(client_file_path, 'r+') as account_file:
        file_content_str = account_file.readline()
        while file_content_str != '':
            parsed_file_str = file_content_str.split('|')
            single_client_name = parsed_file_str[1]
            single_client_num = parsed_file_str[2]
            single_client_balance = parsed_file_str[3]
            single_client_balance = single_client_balance
            dict_item = {str(single_client_name): float(single_client_balance)}
            dict_client_balance.update(dict_item)
            dict_item = {str(single_client_name): long(single_client_num)}
            dict_client_acc_number.update(dict_item)
            file_content_str = account_file.readline()

        if client_name in dict_client_balance.keys():
            if account_change != '':
                dict_item = {str(client_name):  float(dict_client_balance.get(client_name) + float(account_change))}
                dict_client_balance.update(dict_item)
            else:
                print('{} {}'.format(client_name, dict_client_balance.get(client_name)))
        else:
            if account_change == '0.00':
                dict_item = {str(client_name): float(account_change)}
                dict_client_balance.update(dict_item)
                random_number = random.randint(1000000000, 9999999999)
                numbers = []
                for keys in dict_client_acc_number.keys():
                    numbers.append(dict_client_acc_number.get(keys))
                while random_number in numbers:
                    random_number = random.randint(1000000000, 9999999999)
                dict_item = {str(client_name): int(random_number)}
                dict_client_acc_number.update(dict_item)
            elif account_change == '':
                print('No such client')
                return
            else:
                print('Error - invalid operation')
                return
        account_file.seek(0)
        n = 1
        for names in sorted(dict_client_balance.keys()):
            file_content_str = str(n) + '|' + str(names) + '|' + str(dict_client_acc_number.get(names)) + '|' + str(dict_client_balance.get(names)) + '\n'
            account_file.write(file_content_str)
            n += 1
    return

if __name__ == '__main__':
    client_name = raw_input('Enter client name ')
    account_change = raw_input('Enter account change ')
    update_account_file(client_name, account_change)
