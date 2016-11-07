def write_info_to_file(pl_name, pl_score, file_path):
    score_dict = {}
    score_changed = False

    try:
        pl_name = str(pl_name)
    except ValueError:
        return 'Value points is not integer'

    try:
        pl_score = int(pl_score)
    except ValueError:
        return 'Value points is not integer'

    try:
        my_file = open(file_path, 'r+')
    except IOError:
        return 'File cannot be opened'
    else:
        one_line = my_file.readline()

# Converting file content to dictionary        
        while one_line != '':
            pl_name_score = one_line.split(' ')
            score = pl_name_score[1]
            score = score[0: -1]
            pl_name_score[1] = score

            if pl_name_score[0] == pl_name:
                if int(pl_name_score[1]) < pl_score:
                    pl_name_score[1] = pl_score
                    score_changed = True
                else:
                    return ('Lowest score is ignored')
                    my_file.close()

            dict_pair = {pl_name_score[0]: pl_name_score[1]}
            score_dict.update(dict_pair)
            one_line = my_file.readline()

    if score_changed:
        sorted_score_dict = sorted(score_dict, lambda x, y: cmp(int(score_dict[x]), int(score_dict[y])), reverse=True)

    else:
        dict_pair = {pl_name: pl_score}
        score_dict.update(dict_pair)
        sorted_score_dict = sorted(score_dict, lambda x, y: cmp(int(score_dict[x]), int(score_dict[y])), reverse= True)

# writing sorted dictionary to the source file
    my_file.seek(0)
    for item in sorted_score_dict:
        my_file.writelines(str(item) + ' ' + str(score_dict[item])+'\n')

    print 'Player {} is added with {} points'.format(pl_name, pl_score)
    my_file.close()



if __name__ == '__main__':

    pl_name = 'spartak'
    pl_score ='101'
    file_path = 'C:\\temp\\score.txt'
    """
    Expected such structure of the file:
    spartak 90
    dinamo 70
    zenit 50
    rubin 40
    """

    write_info_to_file(pl_name, pl_score, file_path)