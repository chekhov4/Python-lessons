def piglatin(test_string):

    if len(test_string) == 0:
        return ('Zero string')
    splitted_string = test_string.split(' ')
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O']

    for i in range(len(splitted_string)):
        pig_word = list(splitted_string[i])
        firts_vowel = True

        for y in range(len(pig_word)):
            if pig_word[0] not in vowel:
                substitute = pig_word.pop(0)
                pig_word.append(substitute)
                firts_vowel = False
                gggg = pig_word
            else:
                if firts_vowel == True:
                    pig_word.append('way')
                    firts_vowel = True
                    break
                else:
                    pig_word.append('ay')
                    break

        splitted_string[i] =str(''.join(pig_word))

    pigged_string =' '.join(splitted_string)

    return (pigged_string)