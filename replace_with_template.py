def subst_string(source_string, bracket_type, templdate, all):
    result_string =''
    if len(source_string) == 0:
        return ('Zero string')
    i = 0
    while i < len(source_string):

        if source_string[i] == bracket_type[0]:
            y = i+1
            while source_string[y] != bracket_type[1]:
                y +=1

            if all == True:
                result_string += bracket_type[0] + templdate + bracket_type [1]
                i = y+1
                continue

            else:
                result_string += bracket_type[0] + templdate + bracket_type [1]
                result_string += source_string[ y+1:]
                break

        result_string +=source_string[i]
        i += 1


    return (result_string)